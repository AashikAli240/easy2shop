pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/AashikAli240/easy2shop.git'
            }
        }

        stage('Use Minikube Docker') {
            steps {
                bat 'wsl -d Ubuntu bash -c "eval $(minikube docker-env)"'
            }
        }

        stage('Build Docker Image (Inside Minikube)') {
            steps {
                bat 'wsl -d Ubuntu bash -c "cd /mnt/c/ProgramData/Jenkins/.jenkins/workspace/Easy2Shop-CICD && docker build -t easy2shop:latest ."'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                bat 'wsl -d Ubuntu bash -c "kubectl apply -f /mnt/c/ProgramData/Jenkins/.jenkins/workspace/Easy2Shop-CICD/k8s/deployment.yaml"'
            }
        }

        stage('Restart Deployment') {
            steps {
                bat 'wsl -d Ubuntu bash -c "kubectl rollout restart deployment easy2shop-deployment"'
            }
        }
    }
}
