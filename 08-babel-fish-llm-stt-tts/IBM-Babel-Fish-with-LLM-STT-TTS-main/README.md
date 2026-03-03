# IBM-Babel-Fish-with-LLM-STT-TTS

> ⚠️ **Important:** When deploying, you must use your own API key and watsonx Project ID.

IBM Cloud Code Engine is a fully managed, serverless platform for running containerized workloads — no infrastructure management required.

---

## Part 1: Deploy to Skills Network Code Engine (Temporary)

This environment is deleted after a few days and is intended for testing only.

### Step 1 — Create a Code Engine Project

In the left-hand navigation panel, open the **Skills Network Toolbox**, expand the **CLOUD** section, click **Code Engine**, then click **Create Project**.

### Step 2 — Open the Code Engine CLI

On the same page, click **Code Engine CLI**. A new terminal will open, already logged in to your Code Engine project.

### Step 3 — Deploy the Speech-to-Text Service

Run the following command in the Code Engine terminal:

```bash
ibmcloud ce application create --name speech-to-text \
  --env ACCEPT_LICENSE=true \
  --image us.icr.io/sn-labsassets/speech-standalone:latest \
  --port 1080 \
  --registry-secret icr-secret \
  --min-scale 1 \
  --visibility project
```

Once deployed, the terminal will output a URL. Open `worker.py` and replace `base_url` in the `speech_to_text` function with that URL.

<details>
<summary>Parameter reference</summary>

| Parameter | Description |
|---|---|
| `--env` | Passes environment variables to the image. Set `ACCEPT_LICENSE=true` for STT/TTS services. |
| `--image` | Pre-built container image to run. |
| `--port` | Port the application listens on. STT/TTS use port `1080`. |
| `--registry-secret` | Secret for accessing private container images. `icr-secret` is pre-created by Skills Network. |
| `--min-scale` | Minimum number of running instances. `1` ensures the service is always available. |
| `--visibility` | Access scope. `project` makes the service private, accessible only within the project. |

</details>

### Step 4 — Deploy the Text-to-Speech Service

```bash
ibmcloud ce application create --name text-to-speech \
  --env ACCEPT_LICENSE=true \
  --image us.icr.io/sn-labsassets/tts-standalone:latest \
  --port 1080 \
  --registry-secret icr-secret \
  --min-scale 1 \
  --visibility project
```

Once deployed, replace `base_url` in the `text_to_speech` function in `worker.py` with the output URL.

### Step 5 — Deploy Your App

> ⚠️ Set `API_KEY` and `PROJECT_ID` in `worker.py` before running this step.

Make sure you are in the `translator-with-voice-and-watsonx` directory, then run:

```bash
ibmcloud ce application create --name personal-assistant \
  --build-source . \
  --build-context-dir . \
  --image us.icr.io/${SN_ICR_NAMESPACE}/personal-assistant:latest \
  --registry-secret icr-secret \
  --port 8000 \
  --min-scale 1 \
  --visibility project
```

<details>
<summary>Parameter reference</summary>

| Parameter | Description |
|---|---|
| `--build-source` | Source code location. `.` uses the current directory. |
| `--build-context-dir` | Directory within the source that contains the Dockerfile. `.` uses the current directory. |
| `--image` | Target image name that Code Engine will build and push. |

</details>

Once deployed, open the output URL to access your live app.

---

## Part 2: Deploy to Your Own IBM Cloud Account

### Step 1 — Log In to IBM Cloud

```bash
ibmcloud login -u USERNAME
```

> If you have a federated ID, use `ibmcloud login --sso` instead.

Target your resource group:

```bash
ibmcloud target -g Default
```

### Step 2 — Log In to the IBM Entitled Registry

Obtain an entitlement key from the [IBM Container Software Library](https://myibm.ibm.com/products-services/containerlibrary), then:

```bash
IBM_ENTITLEMENT_KEY="YOUR_IBM_ENTITLEMENT_KEY"
echo $IBM_ENTITLEMENT_KEY | docker login -u cp --password-stdin cp.icr.io
```

> The entitlement key is valid for one year as a trial.

### Step 3 — Build the Speech-to-Text Image

```bash
cd /home/project/translator-with-voice-and-watsonx/models/stt
docker build ./speech-to-text -t stt-standalone:latest
```

### Step 4 — Build the Text-to-Speech Image

```bash
cd /home/project/translator-with-voice-and-watsonx/models/tts
docker build ./text-to-speech -t tts-standalone:latest
```

### Step 5 — Create a Namespace and Log In to ICR

```bash
NAMESPACE=personal-assistant
```

```bash
ibmcloud cr region-set global
ibmcloud cr namespace-add ${NAMESPACE}
ibmcloud cr login
```

### Step 6 — Push Watson Images to Your Namespace

```bash
TTS_APPNAME=tts-standalone
STT_APPNAME=stt-standalone
REGISTRY=icr.io
```

```bash
# Text-to-Speech
docker tag ${TTS_APPNAME}:latest ${REGISTRY}/${NAMESPACE}/${TTS_APPNAME}:latest
docker push ${REGISTRY}/${NAMESPACE}/${TTS_APPNAME}:latest

# Speech-to-Text
docker tag ${STT_APPNAME}:latest ${REGISTRY}/${NAMESPACE}/${STT_APPNAME}:latest
docker push ${REGISTRY}/${NAMESPACE}/${STT_APPNAME}:latest
```

### Step 7 — Build and Push the Main App Image

```bash
APP_NAME=watsonx-personal-assistant
```

```bash
cd /home/project/translator-with-voice-and-watsonx
docker build . -t ${APP_NAME}:latest
docker tag ${APP_NAME}:latest ${REGISTRY}/${NAMESPACE}/${APP_NAME}:latest
docker push ${REGISTRY}/${NAMESPACE}/${APP_NAME}:latest
```

### Step 8 — Deploy to Code Engine

> ⚠️ These commands require a credit card to be added to your IBM Cloud account. You will not be charged until you exceed the free tier. See [Code Engine pricing](https://www.ibm.com/cloud/code-engine/pricing) for details.

**1. Target a region and resource group**

Choose the region closest to you or your users (latency scales with distance):

| Region | Location |
|---|---|
| `us-south` | Dallas |
| `us-east` | Washington DC |
| `ca-tor` | Toronto |
| `br-sao` | Sao Paulo |
| `eu-de` | Frankfurt |
| `eu-gb` | London |
| `au-syd` | Sydney |
| `jp-tok` | Tokyo |

```bash
REGION=us-south
RESOURCE_GROUP=Default
ibmcloud target -r ${REGION} -g ${RESOURCE_GROUP}
```

**2. Create and select a Code Engine project**

```bash
ibmcloud ce project create --name personal-assistant
ibmcloud ce project select --name personal-assistant
```

**3. Deploy STT and TTS services**

```bash
ibmcloud ce application create \
  --name ${STT_APPNAME} \
  --port 1080 \
  --min-scale 1 --max-scale 2 \
  --cpu 2 --memory 8G \
  --image private.${REGISTRY}/${NAMESPACE}/${STT_APPNAME}:latest \
  --registry-secret ce-auto-icr-private-${REGION} \
  --visibility project \
  --env ACCEPT_LICENSE=true
```

Replace `base_url` in `speech_to_text` in `worker.py` with the output URL.

```bash
ibmcloud ce application create \
  --name ${TTS_APPNAME} \
  --port 1080 \
  --min-scale 1 --max-scale 2 \
  --cpu 2 --memory 8G \
  --image private.${REGISTRY}/${NAMESPACE}/${TTS_APPNAME}:latest \
  --registry-secret ce-auto-icr-private-${REGION} \
  --visibility project \
  --env ACCEPT_LICENSE=true
```

Replace `base_url` in `text_to_speech` in `worker.py` with the output URL.

**4. Deploy the main app**

```bash
ibmcloud ce application create \
  --name ${APP_NAME} \
  --port 8000 \
  --min-scale 1 --max-scale 2 \
  --cpu 1 --memory 4G \
  --image private.${REGISTRY}/${NAMESPACE}/${APP_NAME}:latest \
  --registry-secret ce-auto-icr-private-${REGION} \
  --env ACCEPT_LICENSE=true
```

Deployment takes a few minutes. The public endpoint URL is printed on success.

**5. Check your deployment**

```bash
ibmcloud ce app list
ibmcloud ce app logs --application ${APP_NAME}
ibmcloud ce app events --application ${APP_NAME}
```

---

## License

The content of this project is licensed under [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0).
