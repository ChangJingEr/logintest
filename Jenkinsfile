pipeline {
  agent any

  stages {
    stage('Install dependencies') {
      steps {
        bat 'pip install -r requirements.txt'
      }
    }

    stage('Run tests') {
      steps {
        bat 'pytest --maxfail=1 --disable-warnings -q'
      }
    }
  }
}
