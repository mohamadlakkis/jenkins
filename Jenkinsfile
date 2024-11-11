pipeline {
  agent any

  environment {
      VIRTUAL_ENV = 'myenv'
      PATH = "/usr/bin/python3:${env.PATH}"
  }

  stages {
      stage('Setup') {
          steps {
              script {
                  if (!fileExists("${env.WORKSPACE}/${VIRTUAL_ENV}")) {
                      sh "python3 -m venv ${VIRTUAL_ENV}"
                  }
                  sh ". ${VIRTUAL_ENV}/bin/activate && pip3 install -r requirements.txt"
              }
          }
      }

      stage('Lint') {
          steps {
              script {
                  sh ". ${VIRTUAL_ENV}/bin/activate && flake8 app.py"
              }
          }
      }

      stage('Test') {
          steps {
              script {
                  sh ". ${VIRTUAL_ENV}/bin/activate && pytest"
              }
          }
      }

      stage('Deploy') {
          steps {
              script {
                  // Deployment logic, e.g., pushing to a remote server
                  echo "Deploying application..."
              }
          }
      }
  }

  post {
      always {
          cleanWs()
      }
  }
}
