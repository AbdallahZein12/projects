export default {
    async fetch(request) {
      if (request.method === "POST" && new URL(request.url).pathname === "/ascii") {
        const boundary = "----WebKitFormBoundary" + Math.random().toString(16).slice(2);
        const CRLF = "\r\n";
  
        const imageBuffer = await request.arrayBuffer();
  
        const preamble = new TextEncoder().encode(
          `--${boundary}${CRLF}` +
          `Content-Disposition: form-data; name="file"; filename="image.jpg"${CRLF}` +
          `Content-Type: image/jpeg${CRLF}${CRLF}`
        );
  
        const postamble = new TextEncoder().encode(`${CRLF}--${boundary}--${CRLF}`);
  
        const fullBody = new Uint8Array(preamble.length + imageBuffer.byteLength + postamble.length);
        fullBody.set(preamble, 0);
        fullBody.set(new Uint8Array(imageBuffer), preamble.length);
        fullBody.set(postamble, preamble.length + imageBuffer.byteLength);
  
        const response = await fetch("https://pic2ascii.liucscs.us/", {
          method: "POST",
          headers: {
            "Content-Type": `multipart/form-data; boundary=${boundary}`
          },
          body: fullBody
        });
  
        const bodyText = await response.text();
  
        try {
          const json = JSON.parse(bodyText);
          return new Response(json.output || "No ASCII returned", {
            headers: { "Content-Type": "text/plain" }
          });
        } catch (e) {
          return new Response("Failed to parse JSON:\n\n" + bodyText, {
            headers: { "Content-Type": "text/plain" }
          });
        }
      }
  
      return new Response("Not Found", { status: 404 });
    }
  }
  