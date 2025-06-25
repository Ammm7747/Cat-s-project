print('Hello from Cat')
{
  "homework": {
    "title": "Загрузка проекта на GitHub и работа с Git",
    "steps": [
      {
        "step": 1,
        "description": "Создать новый репозиторий на GitHub с названием 'Cat-s-project'. Не добавлять README.md через интерфейс GitHub."
      },
      {
        "step": 2,
        "description": "Локально создать папку с проектом, инициализировать в ней git, добавить файл README.md и запушить на GitHub.",
        "commands": [
          "mkdir Cat-s-project",
          "cd Cat-s-project",
          "echo \"# Cat's Project\" > README.md",
          "git init",
          "git add README.md",
          "git commit -m \"Initial commit\"",
          "git remote add origin https://github.com/Ammm7747/Cat-s-project.git",
          "git push -u origin main"
        ]
      },
      {
        "step": 3,
        "description": "Внести локальные изменения — создать файл cat.py, добавить его, закоммитить и отправить в удалённый репозиторий.",
        "commands": [
          "echo \"print('Hello from Cat')\" > cat.py",
          "git add cat.py",
          "git commit -m \"Add cat.py\"",
          "git push"
        ]
      },
      {
        "step": 4,
        "description": "Убедиться, что файл cat.py появился в репозитории на GitHub.",
        "check_url": "https://github.com/Ammm7747/Cat-s-project/blob/main/cat.py"
      }
    ],
    "status": "выполнено",
    "github_repo": "https://github.com/Ammm7747/Cat-s-project"
  }
}
