def commitId

node {
    stage('Preparation') {
        git branch: 'main', url: 'https://github.com/hisrarul/aisight-assignment.git'
    }
    stage('Docker Login') {
        script {
                withCredentials([usernamePassword(credentialsId: '57b60970-cc4d-48b6-be04-beb670b6fedf', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                    sh 'docker login -u $USERNAME -p $PASSWORD'
            }
        }
    }
    stage('Build and Push') {
            commitId = sh (script: 'git rev-parse --short HEAD', returnStdout: true).trim()
            sh """
                docker build -t hisrarul/aisight-assignment:${commitId} -f task-1/Dockerfile .
                docker push hisrarul/aisight-assignment:${commitId}
            """
    }
//     stage('Run Unittest') {
//             sh "docker run hisrarul/aisight-assignment:${commitId}"
//     }
    stage('Deploy to Kubernetes') {
            sh "kubectl create deployment aisight-assignment --image=hisrarul/aisight-assignment:${commitId}"
    }
}
