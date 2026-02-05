pipeline {
    agent any

    environment {
        WSL = 'wsl -d Ubuntu bash -c'
        WORKDIR = '/mnt/c/ProgramData/Jenkins/.jenkins/workspace/Easy2Shop-CICD'
        IMAGE_NAME = 'easy2shop'
        TAG = "${BUILD_NUMBER}"
    }

    stages {

        stage('Checkout Code') {
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
                bat "${WSL} \"cd ${WORKDIR} && docker build -t ${IMAGE_NAME}:${TAG} -t ${IMAGE_NAME}:latest .\""
            }
        }

        stage('Update Deployment YAML Image Tag') {
            steps {
                bat "${WSL} \"sed -i 's|image: easy2shop:.*|image: easy2shop:${TAG}|g' ${WORKDIR}/k8s/deployment.yaml\""
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

        stage('Cleanup Old Images') {
            steps {
                bat "${WSL} \"docker image prune -f\""
            }
        }
    }

    post {
        success {
            echo "🚀 Deployment Successful — Easy2Shop updated with version ${TAG}"
        }
        failure {
            echo "❌ Deployment Failed — Check logs"
        }
    }
}
