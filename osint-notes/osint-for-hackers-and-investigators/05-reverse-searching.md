# Reverse Searching

## Reverse Email

### Free Linux Tools for Email OSINT

#### holehe
- **What it does:** Checks if an email address is attached to an account on over 120 social media and major websites (like Twitter, Instagram, Imgur, etc.).
- **Why it's great:** It is fast, highly accurate, and does not alert the target. It helps you pivot from an email to find their social media usernames.
- **How to install/run:**
```bash
pip install holehe
holehe targetemail@example.com
```

#### GHunt
- **What it does:** An advanced OSINT tool designed specifically for investigating Google accounts.
- **Why it's great:** If your target email is a Gmail address, GHunt can extract the owner's Google ID, YouTube channel, active Google services (like Maps reviews), and sometimes their profile photo and location.
- **How to find it:** Available on the `⁠GHunt GitHub Repository`.

#### SpiderFoot
- **What it does:** A comprehensive OSINT automation platform that integrates dozens of open-source data sources.
- **Why it's great:** You can feed it an email address, and it will automatically query data leak repositories, domain registrars, and web scrapers to build a massive profile on the target completely for free.
- **How to find it:** Available on the ⁠`SpiderFoot Official Website`.

### Completely Free Websites

#### Have I Been Pwned (HIBP)
- **What it does:** Checks if an email address has been compromised in any known data breaches.
- **OSINT Value:** While it won't give you the person's name directly, it tells you exactly which websites they had accounts on (e.g., Adobe, LinkedIn, MySpace). Knowing what services they used provides massive clues for your investigation.
- **Access it here:** ⁠https://haveibeenpwned.com/

#### EPIEOS
- **What it does:** A specialized reverse email lookup tool.
- **OSINT Value:** It allows you to search a Gmail or corporate email address to retrieve associated Google profiles, profile pictures, and related data footprints across the web without paying a dime.
- **Access it here:** https://epieos.com/

#### CyberBackgroundChecks & TruePeopleSearch (US-Only)
- **What it does:** Free public records search engines.
- **OSINT Value:** Unlike BeenVerified, these sites provide a massive amount of address, phone, and email history completely free of charge. Note: You may need a US-based IP address or VPN to access them.
- **Access them here:** ⁠https://www.truepeoplesearch.com/ or ⁠https://www.cyberbackgroundchecks.com/

<br>
<br>

## Reverse Phone

### Free Web-Based Tools
These sites either maintain massive crowdsourced databases or help you find public data without charging fees:

#### ⁠Truecaller (Web Version) 
- By using their web directory (rather than the mobile app, which requires uploading your own contact book), you can search numbers globally for free. It relies on billions of crowdsourced contact lists and is highly accurate for identifying names and spam labels globally.

#### ⁠NumLookup
- A specialized, free web tool built primarily for US-based numbers. It performs API queries directly across telecommunication networks to pull the exact owner name, carrier, and line type without requesting registration.

#### ⁠FastPeopleSearch
- If you are researching a US-based mobile or landline number, this platform provides direct, un-paywalled name histories, current addresses, and associated family member lists for free.

#### ⁠Free Carrier Lookup
- If you don't care about the owner's name but strictly need to verify technical footprints, this tool determines whether a number is active, its specific carrier, and whether it is a VoIP number (like Google Voice) or a real mobile/landline.

#### Search Yellow Directory
- Search Yellow Directory functions as a global Open Source Intelligence (OSINT) and telephone registry tool. Its primary uses include International Reverse Phone Lookup, Global Dialing Assistance, Business & People Directory Access, and International Email Lookup

### Free Linux CLI Tools (OSINT Frameworks)

#### PhoneInfoga
- **What it does:** It scans any international phone number without requiring paid API keys. It analyzes the country code, detects the telecom registry carrier, and automatically executes localized Google Dorks to find where that number has been mentioned across social media, forums, and leaked directories.
- **How to run it:** It can be run straight from your terminal or served as a local Web GUI page on your machine:
```bash
# Download the binary or pull via Docker
docker pull sundowndev/phoneinfoga:latest

# Run a quick scan on a number
docker run --rm -it sundowndev/phoneinfoga scan -n +15551234567
```

#### Social-Scan
- **What it does:** If you manage to link a phone number or an associated username to a targeted target, you can feed it into `social-scan` to instantly check what social platforms (Instagram, Twitter, Pinterest, etc.) have a verified account attached to that exact piece of data.

#### Advanced Google Dorking via Terminal (Using lynx or googler)
Experienced Linux users often bypass third-party websites entirely by using search tools like [⁠Googler](https://github.com/jarun/googler) to perform search queries from the CLI. You can find phone references by wrapping the numbers in specific operators:
- `"555-123-4567"` — Forces Google to find that specific formatting.
- `site:facebook.com "555-123-4567"` — Limits the query entirely to Facebook profiles.
- `filetype:txt OR filetype:csv "555-123-4567"` — Searches for the phone number inside exposed data dumps or public spreadsheets.

### Tip for Reverse Phone Searching
In modern OSINT, standard "reverse lookups" are often blocked by privacy laws or paywalls. Because of this, analysts heavily rely on Pivot Points. For example, if a phone number doesn't yield a name directly, your next step in an investigation is usually to:
1. Try adding the number to a burner contact list on a phone to see if it populates a profile name or photo on **WhatsApp, Signal, or Telegram**.
2. Search the number on **Skype or PayPal** (via the "Send Money" interface) to see if a real name or profile picture is tied to the account.

<br>
<br>

## Deep Fake Detection

### Completely Free Web Tools (No-Cost / High-Utility Triage)

These websites allow you to spot-check files immediately without entering credit card information:

- [⁠BitMind AI Content Detector](https://bitmind.ai/detect): A direct, web-based interface that allows you to instantly upload an image or video to check if it was synthetically generated or altered.

- [⁠FotoForensics](https://fotoforensics.com/): A legendary tool among digital forensic experts and OSINT investigators. Instead of utilizing automated AI detection, it runs **Error Level Analysis (ELA)**. This maps the compression rates across an image. If a face has been digitally pasted or "deepfaked" into an existing photo, the ELA layer will highlight structural anomalies and mismatched pixel density.

- ⁠[Hive Moderation Demo](https://hivemoderation.com/): While Hive is primarily a enterprise API, they offer a highly reliable free browser-based web demo. It allows you to drag and drop single images or video clips to test them against their state-of-the-art synthetic media detection models.

- [⁠Deepware Scanner](https://deepware.ai/): A highly popular open platform focused specifically on finding anomalies in videos. It runs an uploaded clip through multiple open-source deepfake detection models simultaneously to output a unified consensus score.

### Free Linux Tools (Local Python & Command Line Utilities)
Running tools locally on Linux guarantees that the data you are investigating never leaves your machine. These open-source packages require a functional Python environment and are easily deployed via terminal.

#### Open-Source AI Detection Pipelines
- [⁠DeepSecure-AI](https://github.com/Divith123/DeepSecure-AI): A fantastic open-source project hosted on GitHub. It utilizes an EfficientNetV2 backbone coupled with MTCNN face detection and PyTorch. It breaks video files down frame-by-frame, extracts faces, and flags deepfakes locally. It includes a local Gradio web UI that runs directly in your Linux browser.
- [⁠DeepSafe](https://github.com/siddharthksah/DeepSafe): An enterprise-grade, fully open-source platform written in Python and FastAPI. It provides a full backend architecture and dashboard to run local visual and video ensemble models to score deepfake probabilities.
- [⁠Arman176001 / deepfake-detection](https://github.com/Arman176001/deepfake-detection): Specifically built to catch modern deepfakes generated by popular tools like DeepLiveCam and DeepFaceLive. It is written in Python and OpenCV and runs entirely offline on your Linux machine.

#### Media Forensics & Metadata Analysis
True OSINT relies heavily on metadata and origin tracing alongside AI detection:
- **ExifTool:** The ultimate command-line utility for reading, writing, and editing meta information across images and video. By running exiftool video.mp4 on Linux, you can look for software signatures (like Adobe Premiere, generative tools, or unique encoding profiles) that indicate manipulation or a lack of an original camera profile.
- **FFmpeg (Visual Inspection):** The Swiss Army knife of Linux video processing. For deepfake analysis, you can use FFmpeg to split video into individual frames to spot blending artifacts, or extract the audio spectrum to look for voice cuts:
```bash
ffmpeg -i input_video.mp4 -vf "select=not(mod(n\,10))" -vsync vscf frame_%03d.png
```
*(This extracts every 10th frame so you can manually examine skin-edges, eye reflections, and lighting inconsistencies in a photo viewer).*

### Free Linux Tools for Audio Deep Fake Detection
Running local tools ensures that raw audio files (which could be sensitive evidence) never leave your secure Linux environment.

####  Open-Source AI Classifiers (GitHub)
- [media-sec-lab / Audio-Deepfake-Detection](https://github.com/media-sec-lab/Audio-Deepfake-Detection): Hosted on GitHub, this is an excellent, curated master repository containing code, datasets, and pretrained pipelines based on the official academic **ASVspoof Challenge** (the global benchmark for voice spoofing and deepfake detection). It is heavily utilized by researchers deploying automated forensic models locally.

- ⁠[kaifanyu / DeepFake-Audio-Detection](https://github.com/kaifanyu/DeepFake-Audio-Detection): A highly accessible PyTorch- and TensorFlow-based Linux pipeline. It ingests raw audio, extracts features, and runs them through deep learning classification layers to flags clones offline.

- [⁠noorchauhan / DeepFake-Audio-Detection-MFCC](https://github.com/noorchauhan/DeepFake-Audio-Detection-MFCC): This tool converts audio into Mel-Frequency Cepstral Coefficients (MFCCs). MFCCs represent the power spectrum of an audio clip; human vocal tracts produce smooth, continuous transitions, while AI speech generators leave micro-gaps or repetitive digital patterns that this Python library exposes.

#### Signal Analysis & Command Line Utilities
- **SnaffCore / Audacity (via Linux Package Manager):** While Audacity is an open-source GUI tool, installing it via sudo apt install audacity is standard for audio forensics. By switching the track view from "Waveform" to **Spectrogram**, you can visually inspect the clip. AI voice models often struggle with high-frequency noise, leaving a sharp "cutoff" line around 8kHz or 16kHz, or they display unnatural, perfectly vertical energy spikes where an AI-generated word cut in.

- **Praat (Linux Port):** A specialized scientific tool for phonetics used extensively by linguistic forensic experts. You can install it on Linux to map formants, pitch (intonation changes), and jitter/shimmer (micro-instabilities in human vocal cords). AI audio often sounds "too smooth" or lacks the chaotic micro-instabilities of a real human throat.

- **FFmpeg (Audio Extraction & Metadata Analysis):** Essential for pulling uncompressed audio streams out of raw social media video files before feeding them into detectors:
```bash
ffmpeg -i target_video.mp4 -vn -acodec pcm_s16le -ar 16000 output_audio.wav
```
*(This extracts the video's audio, strips out container artifacts, and encodes it into a clean, uncompressed 16kHz WAV format ideal for local Python detection scripts).*