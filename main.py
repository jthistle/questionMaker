
import os
import re
import base64


def main():
    SRC_HTML = "./index_src.html"
    DEST_HTML = "./final/index.html"
    QUESTIONS_DIR = "./questions"
    bold_re = re.compile(r"(?:\*\*(.*?)\*\*)|(?:__(.*?)__)", re.I);
    italic_re = re.compile(r"(?:\*(.*?)\*)|(?:_(.*?)_)", re.I);
    image_re = re.compile(r"!\[([^\]\n]*)\]\(([^\)\n]+)\)", re.I);
    linebr_re = re.compile("\n\n+", re.M)
    ul_re = re.compile(r"\n((?:[-*]\s.*?\n)+)", re.I);
    ul_li_re = re.compile(r"\n\s*[-*]\s(.*)", re.I);
    ol_re = re.compile(r"\n((?:\d\.\s.*?\n)+)", re.I);
    ol_li_re = re.compile(r"\n\s*\d\.\s(.*)", re.I);

    inject_html = ""
    i = 0
    questions = os.listdir(QUESTIONS_DIR)
    for q in questions:
        if q[-3:] != ".md":
            continue
        
        file_path = os.path.join(QUESTIONS_DIR, q)
        with open(file_path, "r") as qfile:
            q_src = qfile.read()

            replace = []
            for match in image_re.finditer(q_src):
                img = match.group(2)
                with open(os.path.join(QUESTIONS_DIR, img), "rb") as imagefile:
                    b64 = base64.b64encode(imagefile.read())

                parts = img.split(".")
                if len(parts) == 1:
                    ext = "png"
                else:
                    ext = parts[-1]
                replacement = '<img alt="{}" src="data:image/{};base64, {}" />'.format(
                    match.group(1), ext, b64.decode("ascii")
                )
                replace.append((match.span(), replacement))

            sanitised = "\n" + q_src
            replace.reverse()
            for x in replace:
                sanitised = sanitised[:x[0][0]] + x[1] + sanitised[x[0][1]+1:]

            sanitised = ul_re.sub(r"<ul>\n\1</ul>", sanitised)
            sanitised = ul_li_re.sub(r"<li>\1</li>", sanitised)

            sanitised = ol_re.sub(r"<ol>\n\1</ol>", sanitised)
            sanitised = ol_li_re.sub(r"<li>\1</li>", sanitised)

            sanitised = "<p>" + sanitised
            sanitised = linebr_re.sub("</p><p>", sanitised)
            sanitised += "</p>"

            sanitised = bold_re.sub(r"<b>\1\2</b>", sanitised)
            sanitised = italic_re.sub(r"<i>\1\2</i>", sanitised)

            inject_html += """
<!-- from {path} -->
<div class="question" id="question{n}">
  {txt}
  <p class="questionNum">Question no. {rn}</span>
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