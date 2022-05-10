pipeline{
        agent any
        stages{
            stage('Requirements'){
                steps{
                    sh "sudo apt update"
                    sh "sudo apt install python3"
                    sh "sudo apt install python3-pip"
                    sh "pip3 install -r requirements.txt"
                    sh "sudo apt install curl -y"
                    sh "sudo apt install -y curl jq"
                    sh "curl https://get.docker.com | sudo bash"
                    sh "version=$(curl -s https://api.github.com/repos/docker/compose/releases/latest | jq -r '.tag_name')"
                    sh "sudo curl -L "https://github.com/docker/compose/releases/download/${version}/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose"
                    sh "sudo chmod +x /usr/local/bin/docker-compose"
                }
            }
            stage('Docker build and push'){
                steps{
                    sh "docker-compose up -d "
                    sh "docker build"
                    sh "docker push"
                }
            stage('Deploy'){
                steps{
                    sh "curl localhost:5000"
                }
            }
        }
}