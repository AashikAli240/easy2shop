pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/AashikAli240/easy2shop.git'
            }
        }

        stage('Use Minikube Docker Daemon') {
            steps {
                bat 'wsl -d Ubuntu bash -c "eval $(minikube docker-env)"'
            }
        }

        stage('Build Docker Image (Inside Minikube)') {
            steps {
                bat 'wsl -d Ubuntu bash -c "cd /mnt/c/Users/%USERNAME%/projects/easy2shop && docker build -t easy2shop:latest ."'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                withCredentials([file(credentialsId: 'kubeconfig-easy2shop', variable: 'KCFG')]) {
                    bat """
                        wsl -d Ubuntu bash -c "kubectl --kubeconfig=/mnt/c/Users/%USERNAME%/kubeconfig-easy2shop apply -f /mnt/c/Users/%USERNAME%/projects/easy2shop/k8s/"
                    """
                }
            }
        }
    }
}
