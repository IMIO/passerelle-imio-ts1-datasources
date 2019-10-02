@Library('eo-jenkins-lib@master') import eo.Utils

pipeline {
    agent any
    stages {
        stage('Packaging') {
            steps {
                script {
                    if (env.JOB_NAME == 'passerelle-imio-ts1-datasources' && env.GIT_BRANCH == 'origin/master') {
                        sh 'sudo -H -u eobuilder /usr/local/bin/eobuilder -d stretch passerelle-imio-ts1-datasources'
                    } else if (env.GIT_BRANCH.startsWith('hotfix/')) {
                        sh "sudo -H -u eobuilder /usr/local/bin/eobuilder -d stretch --branch ${env.GIT_BRANCH} --hotfix passerelle-imio-ts1-datasources"
                    }
                }
            }
        }
    }
    post {
        always {
            script {
                utils = new Utils()
                utils.mail_notify(currentBuild, env, 'ci+jenkins-passerelle-imio-ts1-datasources@entrouvert.org')
            }
        }
        success {
            cleanWs()
        }
    }
}
