pipeline {
    agent any

    environment {
        IMAGE_NAME = "santhiyakrishdevops/grocery-app"
        CONTAINER_NAME = "grocery-app"
    }

    stages {

        stage('Clone Code') {
            steps {
                git 'https://github.com/SanthiyaK/online-grocery-ci-cd'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:latest .'
            }
        }

        stage('Push Image to Docker Hub') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-creds',
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_PASS'
                    )
                ]) {
                    sh '''
                        echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                        docker push $IMAGE_NAME:latest
                    '''
                }
            }
        }

        stage('Deploy on EC2') {
            steps {
                sh '''
                    docker rm -f $CONTAINER_NAME || true
                    docker pull $IMAGE_NAME:latest
                    docker run -d \
                      --name $CONTAINER_NAME \
                      -p 5000:5000 \
                      $IMAGE_NAME:latest
                '''
            }
        }
    }
}
