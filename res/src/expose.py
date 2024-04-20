"""
Code credits: ColabKobold

https://github.com/lostruins/koboldcpp
"""

import os, sys, threading, time, subprocess, re

def create_cloudflare_tunnel(port: int):

    """
    Create a cloudflare tunnel for the server
    """

    try:

        def run_tunnel():
            
            """
            Run the cloudflare tunnel
            """

            # variables to be used in the thread
            tunnel_process = None
            tunnel_output = ""
            tunnel_raw_dump = ""

            time.sleep(0.2)
            if os.name == 'nt':

                print("Starting Cloudflare Tunnel for Windows, please wait...", flush=True)
                tunnel_process = subprocess.Popen(f"cloudflared.exe tunnel --url localhost:{port}", text=True, encoding='utf-8', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
            
            elif sys.platform=="darwin":
                print("Starting Cloudflare Tunnel for MacOS, please wait...", flush=True)
                tunnel_process = subprocess.Popen(f"./cloudflared tunnel --url http://localhost:{port}", text=True, encoding='utf-8', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
            
            else:
                print("Starting Cloudflare Tunnel for Linux, please wait...", flush=True)
                tunnel_process = subprocess.Popen(f"./cloudflared-linux-amd64 tunnel --url http://localhost:{port}", text=True, encoding='utf-8', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
            
            # wait for the tunnel to be ready
            time.sleep(10)

            def tunnel_reader():

                """
                Read the stderr of the cloudflare tunnel process
                """

                nonlocal tunnel_process, tunnel_output, tunnel_raw_dump

                pattern: str = r'https://[\w\.-]+\.trycloudflare\.com'

                while True:

                    line = tunnel_process.stderr.readline() #cloudflare writes to stderr for some reason
                    tunnel_raw_dump += line+"\n"

                    if not line:

                        # if the line is empty, the tunnel is closed
                        return
                    
                    found = re.findall(pattern, line)

                    for x in found:

                        tunneloutput = x

                        return

            tunnel_reader_thread = threading.Thread(target=tunnel_reader)
            tunnel_reader_thread.start()

            time.sleep(5) # wait for the tunnel to be ready

            if tunnel_output=="":

                print(f"Error: Could not create cloudflare tunnel!\nMore Info:\n{tunnel_raw_dump}", flush=True)

            time.sleep(0.5)
            tunnel_process.wait()

        # Windows
        if os.name == 'nt':

            if os.path.exists("cloudflared.exe") and os.path.getsize("cloudflared.exe") > 1000000:

                print("Cloudflared file exists, reusing it...")

            else:

                print("Downloading Cloudflare Tunnel for Windows...")
                subprocess.run("curl -fL https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-windows-amd64.exe -o cloudflared.exe", shell=True, capture_output=True, text=True, check=True, encoding='utf-8')
        
        # MacOS
        elif sys.platform=="darwin":

            if os.path.exists("cloudflared") and os.path.getsize("cloudflared") > 1000000:
                print("Cloudflared file exists, reusing it...")

            else:

                print("Downloading Cloudflare Tunnel for MacOS...")
                subprocess.run("curl -fL https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-darwin-amd64.tgz -o cloudflared-darwin-amd64.tgz", shell=True, capture_output=True, text=True, check=True, encoding='utf-8')
                subprocess.run("tar -xzf cloudflared-darwin-amd64.tgz", shell=True)
                subprocess.run("chmod +x 'cloudflared'", shell=True)

        else:

            if os.path.exists("cloudflared-linux-amd64") and os.path.getsize("cloudflared-linux-amd64") > 1000000:
                print("Cloudflared file exists, reusing it...")

            else:

                print("Downloading Cloudflare Tunnel for Linux...")
                subprocess.run("curl -fL https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 -o cloudflared-linux-amd64", shell=True, capture_output=True, text=True, check=True, encoding='utf-8')
                subprocess.run("chmod +x 'cloudflared-linux-amd64'", shell=True)

        print("Attempting to start tunnel thread...", flush=True)
        tunnel_thread = threading.Thread(target=run_tunnel)
        tunnel_thread.start()

    except Exception as ex:

        print("Remote Tunnel Failed!")
        print(str(ex))
        return None
    
