# Para contribuir para o livro:

 1. Instalar requirements.txt
 2. Adicionar uma nova sub-pasta à pasta content 
    - Seguir modelo das pastas guide, objects e math
 3. Adicionar o novo conteúdo ao arquivo *_toc.yml*
 4. Executar ```jupyter-book build content```
    - Os arquivos resultantes vão para a pasta _build
 5. Para ver o resultado antes de mandar para o github: ```firefox _build/html/index.html```
 6. Push para o master
 7. Executar ```ghp-import -n -p -f _build/html``` para atualizar a página no github




