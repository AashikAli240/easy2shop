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

        stage('Build Docker Image (Inside Minikube)') {
            steps {
                bat """
                ${WSL} "
                    eval \$(minikube docker-env) &&
                    cd ${WORKDIR} &&
                    docker build -t easy2shop:latest .
                "
                """
            }
        }

        stage('Update Deployment Image') {
            steps {
                bat """
                ${WSL} "
                    eval \$(minikube docker-env) &&
                    kubectl set image deployment/easy2shop-deployment easy2shop=easy2shop:latest --record
                "
                """
            }
        }

        stage('Verify Rollout') {
            steps {
                bat """
                ${WSL} "kubectl rollout status deployment/easy2shop-deployment"
                """
            }
        }
    }

    post {
        success {
            echo "🚀 Deployment Successful — Easy2Shop updated"
        }
        failure {
            echo "❌ Deployment Failed — Check logs"
        }
    }
}
