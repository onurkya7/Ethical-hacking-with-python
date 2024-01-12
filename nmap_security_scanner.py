import subprocess

def automated_security_scan(target_host):
    try:
        # Run Nmap scan and capture both standard output and standard error
        result = subprocess.run(
            ["C:\\Program Files (x86)\\Nmap\\nmap.exe", "-p-", "-T4", "--open", "--script", "vuln", "-oN", "scan_results.txt", target_host],
            capture_output=True,
            text=True
        )

        # Print the standard output
        print("Nmap Output:")
        print(result.stdout)

        # Check for errors in the standard error
        if result.stderr:
            print("Nmap Error:")
            print(result.stderr)

        print("Scan completed. Results have been saved to scan_results.txt.")
    except Exception as e:
        print(f"Error: {e}")

target_host = "example.com"
automated_security_scan(target_host)
