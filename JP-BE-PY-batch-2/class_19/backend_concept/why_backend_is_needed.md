# Frontend Code Vulnerabilities

Frontend code can be easily viewed, modified, or exploited by malicious users since it's delivered to their devices.

## Key Risks

- **API Keys & Credentials**: Storing secrets, such as API keys or database credentials, on the frontend would expose them to anyone inspecting the code, which is a serious security flaw.

- **Trust**: Any data or logic handled exclusively on the frontend is under the control of the client (the user). This can lead to untrustworthy data since malicious users could tamper with it before sending it to a server.

- **Handling Complex Computations**: Computationally intensive tasks can be too burdensome for the frontend. Offloading these tasks to the backend ensures the frontend remains responsive.

- **Multiple Frontends**: Every frontend would need to duplicate the same logic and interact with the data directly, leading to inefficiency and duplication of effort.

- **Protected Business Logic**: Keeping critical business logic (like pricing rules, discount calculations, or access permissions) on the backend prevents users from tampering with the application’s behavior.
