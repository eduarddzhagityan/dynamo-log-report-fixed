Parse the Apache-style access log at /app/access.log and write a JSON report to /app/report.json.

The report must be a JSON object with exactly these three keys:
- total_requests: integer count of non-empty log lines
- unique_ips: integer count of distinct client IP addresses, using the first whitespace-delimited field on each non-empty line
- top_path: string request path with the highest number of occurrences, parsed from the quoted HTTP request line

Success criteria:
1. /app/report.json exists, is valid JSON, and contains exactly the keys total_requests, unique_ips, and top_path.
2. total_requests is 6.
3. unique_ips is 3.
4. top_path is /index.html.
