# import os
# import subprocess



# project_path = r"resume_generator"

# os.chdir(project_path)
# subprocess.run("npm start", shell=True)




import os
import subprocess

def start_node_server():
    # Get the directory where this script is located
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Full path to server.js
    server_file = os.path.join(current_dir, "server.js")

    if not os.path.exists(server_file):
        print("Error: server.js not found in the current directory.")
        return

    # Change directory and run the Node.js server
    os.chdir(current_dir)
    print("Starting Node.js server from:", current_dir)
    subprocess.run(["node", server_file], shell=True)

# # if __name__ == "__main__":




# def start_node_server():
#     current_dir = os.path.dirname(os.path.abspath(__file__))
#     server_file = os.path.join(current_dir, "server.js")

#     if not os.path.exists(server_file):
#         print("Error: server.js not found in the current directory.")
#         return

#     os.chdir(current_dir)
#     print("Starting Node.js server from:", current_dir)

#     subprocess.Popen(["node", server_file], shell=True)  # Non-blocking


# start_node_server()
