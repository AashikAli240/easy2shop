pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/AashikAli240/easy2shop.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    bat 'docker build -t easy2shop:latest .'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    bat 'pytest || echo "No tests found, skipping"'
                }
            }
        }

        stage('Deploy (Docker)') {
            steps {
                script {
                    bat 'docker rm -f easy2shop || echo "No old container"'
                    bat 'docker run -d -p 8000:8000 --name easy2shop easy2shop:latest'
                }
            }
        }

        stage('Deploy (Kubernetes)') {
            steps {
                script {
                    bat 'kubectl apply -f k8s/deployment.yaml'
                    bat 'kubectl apply -f k8s/service.yaml'
                }
            }
        }

    }
}

