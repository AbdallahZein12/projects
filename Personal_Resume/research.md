# research.md

**1. What is a Cloudflare Worker?**  
A Cloudflare Worker is a lightweight serverless function that runs at the edge of Cloudflare’s global network, allowing developers to handle requests closer to the user without provisioning traditional backend servers.

**2. How does a Worker handle HTTP requests and return responses?**  
A Worker listens for incoming HTTP requests using the `fetch` event and returns responses using the `Response` object, allowing custom logic to manipulate headers, body content, and routing.

**3. What is Cloudflare D1? What are some pros and cons of using it?**  
Cloudflare D1 is a serverless SQL database built on SQLite and integrated into the Cloudflare Workers ecosystem.  
**Pros:** Easy to use, close to edge functions, low latency.  
**Cons:** Not ideal for high-throughput write operations or massive datasets due to SQLite limitations.

**4. How does client-side JavaScript call an external API?**  
Client-side JavaScript can call an external API using the `fetch()` function or libraries like `axios`, sending HTTP requests and handling responses asynchronously using promises or `async/await`.

**5. What is the benefit of deploying APIs to the edge instead of traditional servers?**  
Deploying APIs to the edge reduces latency by running code geographically closer to users, improves scalability, and offloads traffic from centralized servers, enabling faster response times and better resilience.
