# ASCII Art API with Cloudflare Worker + Flask

This project allows users to upload an image via a Flask web interface, which is then forwarded to a Cloudflare Worker. The Worker sends the image to a separate backend service (`pic2ascii.liucscs.us`) that processes the image and returns an ASCII representation of it. The result is displayed back on the original site (`abdallah.liucscs.us`).

---

## 🔧 How It Works

1. **User uploads an image** on the `/ascii-art` page on `abdallah.liucscs.us`.
2. **Flask receives the image** and sends it as a POST request to a Cloudflare Worker at `worker1.liucscs.us/ascii`.
3. The **Cloudflare Worker formats the image** as `multipart/form-data` and sends it to `https://pic2ascii.liucscs.us/`.
4. `pic2ascii` (a separate Flask service) generates the **ASCII art** and returns it as JSON.
5. The **Worker extracts the ASCII output** and sends it back to Flask.
6. Flask **displays the ASCII art** to the user on the same page.

---

## 📁 File Structure

- `worker.js`: Cloudflare Worker script that acts as a middleware API layer.
- `app.py`: Flask backend with the `/ascii-art` route.
- `templates/upload.html`: HTML form for image upload + result display.
- `pic2ascii.liucscs.us`: Separate project that actually converts images to ASCII (already hosted).

---

## 🌐 Cloudflare Worker

The Worker lives at:
https://worker1.liucscs.us/ascii


It accepts POST requests with JPEG image data and forwards it to:
https://pic2ascii.liucscs.us/


The image is sent as form-data with the `file` field, as expected by the Flask service.

---

## 🛠️ Technologies Used

- **Flask** (Python)
- **Cloudflare Workers** (JavaScript)
- **HTML/CSS (Jinja2 template)** for the frontend
- **Cloudflare Tunnel** to expose the Flask service securely

---

## 📦 Example Request Flow

```http
POST /upload (image upload)
↓
Flask forwards image → worker1.liucscs.us/ascii
↓
Worker sends form-data → pic2ascii.liucscs.us
↓
ASCII art returned → displayed in HTML

