
import os
import re
import base64


def main():
    SRC_HTML = "./index_src.html"
    DEST_HTML = "./final/index.html"
    QUESTIONS_DIR = "./questions"
    questions = os.listdir(QUESTIONS_DIR)
    image_re = re.compile(r"!\[([^\]\n]*)\]\(([^\)\n]+)\)", re.I);
    linebr_re = re.compile("\n\n+", re.M)

    inject_html = ""
    i = 0
    for q in questions:
        if q[-3:] != ".md":
            continue
        
        file_path = os.path.join(QUESTIONS_DIR, q)
        with open(file_path, "r") as qfile:
            q_src = qfile.read()

            replace = []
            for match in image_re.finditer(q_src):
                with open(os.path.join(QUESTIONS_DIR, match.group(2)), "rb") as imagefile:
                    b64 = base64.b64encode(imagefile.read())
                replacement = '<img alt="{}" src="data:image/png;base64, {}" />'.format(
                    match.group(1), b64.decode("ascii")
                )
                replace.append((match.span(), replacement))

            sanitised = q_src
            replace.reverse()
            for x in replace:
                sanitised = sanitised[:x[0][0]] + x[1] + sanitised[x[0][1]:]

            sanitised = linebr_re.sub("<br />", sanitised)

            inject_html += """
<!-- from {path} -->
<div class="question" id="question{n}">
  {txt}
  <br /><span class="questionNum">Question no. {rn}</span>
</div>""".format(path=file_path, n=i, rn=i+1, txt=sanitised)

        i += 1

    inject_html += """
<div id="questionCount" style="display: none;">{}</div>
""".format(i)

    with open(SRC_HTML, "r") as file:
        contents = file.read()
        contents = contents.replace("<!-- REPLACE ME -->", inject_html)
    
    with open(DEST_HTML, "w") as file:
        file.write(contents)


if __name__ == "__main__":
    main()