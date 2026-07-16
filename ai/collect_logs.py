import subprocess

def run(command):
    try:
        return subprocess.check_output(
            command,
            shell=True,
            text=True,
            stderr=subprocess.STDOUT
        )
    except subprocess.CalledProcessError as e:
        return e.output


logs = {}

logs["docker_ps"] = run("docker ps -a")

logs["compose_ps"] = run("docker compose ps")

logs["app_logs"] = run("docker logs spring-petclinic")

logs["mysql_logs"] = run("docker logs mysql")


with open("deployment_logs.txt","w") as f:

    for key,value in logs.items():

        f.write("="*60+"\n")

        f.write(key+"\n")

        f.write("="*60+"\n")

        f.write(value+"\n\n")


print("Logs collected successfully.")
