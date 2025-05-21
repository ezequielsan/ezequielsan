import requests
import os

GITHUB_USERNAME = os.environ["GITHUB_USERNAME"]
GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]
README_PATH = "README.md"

headers = {
    "Authorization": f"token {GITHUB_TOKEN}"
}

# Linguagens conhecidas e suas badges (adicione mais se quiser)
LANG_BADGES = {
    "Python": "![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)",
    "JavaScript": "![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)",
    "TypeScript": "![TypeScript](https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white)",
    "Java": "![Java](https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=openjdk&logoColor=white)",
    "C": "![C](https://img.shields.io/badge/C-00599C?style=for-the-badge&logo=c&logoColor=white)",
    "C++": "![C++](https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white)",
    "HTML": "![HTML](https://img.shields.io/badge/HTML-E34F26?style=for-the-badge&logo=html5&logoColor=white)",
    "CSS": "![CSS](https://img.shields.io/badge/CSS-1572B6?style=for-the-badge&logo=css3&logoColor=white)",
    "Shell": "![Shell](https://img.shields.io/badge/Shell-121011?style=for-the-badge&logo=gnu-bash&logoColor=white)",
    "Go": "![Go](https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white)",
    "Haskell": "![Haskell](https://img.shields.io/badge/Haskell-5e5086?style=for-the-badge&logo=haskell&logoColor=white)",
    "Kotlin": "![Kotlin](https://img.shields.io/badge/Kotlin-7F52FF?style=for-the-badge&logo=kotlin&logoColor=white)",
    "Rust": "![Rust](https://img.shields.io/badge/Rust-000000?style=for-the-badge&logo=rust&logoColor=white)",
    "PHP": "![PHP](https://img.shields.io/badge/PHP-777BB4?style=for-the-badge&logo=php&logoColor=white)",
    "Ruby": "![Ruby](https://img.shields.io/badge/Ruby-CC342D?style=for-the-badge&logo=ruby&logoColor=white)",
    "Perl": "![Perl](https://img.shields.io/badge/Perl-39457E?style=for-the-badge&logo=perl&logoColor=white)",
    "Scala": "![Scala](https://img.shields.io/badge/Scala-DC322F?style=for-the-badge&logo=scala&logoColor=white)",
    "Swift": "![Swift](https://img.shields.io/badge/Swift-FA7343?style=for-the-badge&logo=swift&logoColor=white)",
    "Dart": "![Dart](https://img.shields.io/badge/Dart-0175C2?style=for-the-badge&logo=dart&logoColor=white)",
    "Elixir": "![Elixir](https://img.shields.io/badge/Elixir-4B275F?style=for-the-badge&logo=elixir&logoColor=white)",
    "R": "![R](https://img.shields.io/badge/R-276DC3?style=for-the-badge&logo=r&logoColor=white)",
    "MATLAB": "![MATLAB](https://img.shields.io/badge/MATLAB-0076A8?style=for-the-badge&logo=mathworks&logoColor=white)",
    "Assembly": "![Assembly](https://img.shields.io/badge/Assembly-6E4C13?style=for-the-badge&logo=assembly&logoColor=white)",
    "F#": "![F#](https://img.shields.io/badge/F%23-378BBA?style=for-the-badge&logo=fsharp&logoColor=white)",
    "Objective-C": "![Objective-C](https://img.shields.io/badge/Objective--C-438EFF?style=for-the-badge&logo=apple&logoColor=white)",
    "Visual Basic": "![Visual Basic](https://img.shields.io/badge/Visual%20Basic-5C2D91?style=for-the-badge&logo=visual-basic&logoColor=white)",
    "Fortran": "![Fortran](https://img.shields.io/badge/Fortran-734F96?style=for-the-badge&logo=fortran&logoColor=white)",
    "COBOL": "![COBOL](https://img.shields.io/badge/COBOL-00599C?style=for-the-badge&logo=cobol&logoColor=white)",
    "Groovy": "![Groovy](https://img.shields.io/badge/Groovy-4298B8?style=for-the-badge&logo=apache-groovy&logoColor=white)",
    "Lua": "![Lua](https://img.shields.io/badge/Lua-2C2D72?style=for-the-badge&logo=lua&logoColor=white)",
    "Erlang": "![Erlang](https://img.shields.io/badge/Erlang-A90533?style=for-the-badge&logo=erlang&logoColor=white)",
    "Clojure": "![Clojure](https://img.shields.io/badge/Clojure-5881D8?style=for-the-badge&logo=clojure&logoColor=white)",
    "Vim": "![Vim](https://img.shields.io/badge/Vim-019733?style=for-the-badge&logo=vim&logoColor=white)",
    "Emacs": "![Emacs](https://img.shields.io/badge/Emacs-7F5AB6?style=for-the-badge&logo=gnu-emacs&logoColor=white)",
    "VS Code": "![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)",
    "IntelliJ IDEA": "![IntelliJ IDEA](https://img.shields.io/badge/IntelliJ%20IDEA-000000?style=for-the-badge&logo=intellij-idea&logoColor=white)",
    "Eclipse": "![Eclipse](https://img.shields.io/badge/Eclipse-2C2255?style=for-the-badge&logo=eclipse&logoColor=white)",
    "NetBeans": "![NetBeans](https://img.shields.io/badge/NetBeans-1B6AC6?style=for-the-badge&logo=apache-netbeans-ide&logoColor=white)",
    "Xcode": "![Xcode](https://img.shields.io/badge/Xcode-147EFB?style=for-the-badge&logo=xcode&logoColor=white)",
    "Android Studio": "![Android Studio](https://img.shields.io/badge/Android%20Studio-3DDC84?style=for-the-badge&logo=android-studio&logoColor=white)",
    "PyCharm": "![PyCharm](https://img.shields.io/badge/PyCharm-000000?style=for-the-badge&logo=pycharm&logoColor=white)",
    "RStudio": "![RStudio](https://img.shields.io/badge/RStudio-75AADB?style=for-the-badge&logo=rstudio&logoColor=white)",
    "Atom": "![Atom](https://img.shields.io/badge/Atom-66595C?style=for-the-badge&logo=atom&logoColor=white)",
    "Sublime Text": "![Sublime Text](https://img.shields.io/badge/Sublime%20Text-FF9800?style=for-the-badge&logo=sublime-text&logoColor=white)",
    "Notepad++": "![Notepad++](https://img.shields.io/badge/Notepad++-90E59A?style=for-the-badge&logo=notepad%2B%2B&logoColor=black)",
    "Vagrant": "![Vagrant](https://img.shields.io/badge/Vagrant-1563FF?style=for-the-badge&logo=vagrant&logoColor=white)",
    "Ansible": "![Ansible](https://img.shields.io/badge/Ansible-EE0000?style=for-the-badge&logo=ansible&logoColor=white)",
    "Docker": "![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)",
    "Kubernetes": "![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)",
    "Terraform": "![Terraform](https://img.shields.io/badge/Terraform-623CE4?style=for-the-badge&logo=terraform&logoColor=white)",
    "Jenkins": "![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=for-the-badge&logo=jenkins&logoColor=white)",
    "Travis CI": "![Travis CI](https://img.shields.io/badge/Travis%20CI-3EAAAF?style=for-the-badge&logo=travis-ci&logoColor=white)",
}
 


def get_repos(username):
    repos = []
    page = 1
    while True:
        url = f"https://api.github.com/users/{username}/repos?per_page=100&page={page}"
        response = requests.get(url, headers=headers)
        data = response.json()
        if not data:
            break
        repos.extend(data)
        page += 1
    return repos

def get_languages(repo_full_name):
    url = f"https://api.github.com/repos/{repo_full_name}/languages"
    response = requests.get(url, headers=headers)
    return list(response.json().keys())

def generate_badges(languages):
    badges = []
    for lang in sorted(set(languages)):
        if lang in LANG_BADGES:
            badges.append(LANG_BADGES[lang])
        else:
            # Badge genérico se não estiver no mapeamento
            badges.append(f"![{lang}](https://img.shields.io/badge/{lang.replace('+', '%2B')}-gray?style=for-the-badge)")
    return "\n".join(badges)

def main():
    repos = get_repos(GITHUB_USERNAME)
    all_languages = []

    for repo in repos:
        if not repo['fork']:
            all_languages.extend(get_languages(repo['full_name']))
            print(f"✅ Linguagens do repositório {repo['name']} obtidas com sucesso.")
            print(f"   Linguagens: {', '.join(all_languages)}")

    badge_block = generate_badges(all_languages)
    badge_block += "\n![Figma](https://img.shields.io/badge/figma-%23F24E1E.svg?style=for-the-badge&logo=figma&logoColor=white)\n"
    badge_block += "![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)\n"
    badge_block += "![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)\n"
    badge_block += "![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)\n"
    badge_block += "![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)\n"
    badge_block += "![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)\n"

    with open(README_PATH, 'r', encoding='utf-8') as file:
        content = file.read()

    # Encontrar seção de tools e sobrescrever
    start_marker = "### Languages and tools"
    end_marker = "### Currently studying"

    start_index = content.find(start_marker)
    end_index = content.find(end_marker)

    if start_index == -1 or end_index == -1:
        print("❌ Marcadores não encontrados. Abortando atualização.")
        return

    before = content[:start_index + len(start_marker)]
    after = content[end_index:]

    new_section = f"\n\n{badge_block}\n\n"

    updated_content = before + new_section + after

    with open(README_PATH, 'w', encoding='utf-8') as file:
        file.write(updated_content)

    print("✅ README atualizado com sucesso!")

if __name__ == "__main__":
    main()
