pipeline {
    agent any

    environment {
        WSL = 'wsl -d Ubuntu bash -c'
        WORKDIR = '/mnt/c/ProgramData/Jenkins/.jenkins/workspace/Easy2Shop-CICD'
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/AashikAli240/easy2shop.git'
            }
        }

        stage('Configure Minikube Docker') {
            steps {
                bat "${WSL} \"eval \$(minikube docker-env)\""
            }
        }

        stage('Build Docker Image (Inside Minikube)') {
            steps {
                bat "${WSL} \"cd ${WORKDIR} && docker build -t easy2shop:latest .\""
            }
        }

        stage('Apply Kubernetes Deployment') {
            steps {
                bat "${WSL} \"kubectl apply -f ${WORKDIR}/k8s/deployment.yaml\""
            }
        }

        stage('Restart Deployment') {
            steps {
                bat "${WSL} \"kubectl rollout restart deployment easy2shop-deployment\""
            }
        }

        stage('Verify Rollout') {
            steps {
                bat "${WSL} \"kubectl rollout status deployment/easy2shop-deployment\""
            }
        }
    }

    post {
        success {
            echo "🚀 Deployment Successful — Easy2Shop updated on Kubernetes"
        }
        failure {
            echo "❌ Deployment Failed — Check logs"
        }
    }
}
