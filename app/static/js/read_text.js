 //if user input the data, always do this function
 function updateValue(e) {
    encode = "";
    var code = editor.getValue();
    // const regexp =  /<!--.+-->/g;
    code_list = code.split(/\r\n|\n/);
    // "" delete
    code_list = code_list.filter(Boolean)
    // String of commentout user input
    let program_code = "";
    let mutch_number = 0;
    let commentoutnum = 0;
    //list
    // console.log(code_list)
    for (let i = 0; i < code_list.length; i++) {
      // Is this in the commentout?
     // console.log(document.getElementsByClassName("ace_comment")[commentoutnum])
      // ace_commentが存在するか確認
      if (document.getElementsByClassName("ace_comment")[commentoutnum] != null) {
        // ace_commentがコメントアウトの行と一致するか確認
        if (document.getElementsByClassName("ace_comment")[commentoutnum].textContent === code_list[i]) {
          //commentout　取得
          m = document.getElementsByClassName("ace_comment")[commentoutnum].textContent
         // console.log(i, document.getElementsByClassName("ace_comment")[commentoutnum].textContent, code_list[i])
          // Commentout 確認
          commentoutnum += 1;
          let commentout = "";
          // list -> string
          mutch_number += 1;
          //  m = String(code_list[i].match(regexp))
          let [a,b] = commentoutSystem(m,commentout)
          let lista = [a,b]
          m = lista[0];
          commentout = lista[1];

          let nd_code_data = [{
            "type": "text",
            "data": {
              "text": escapeHtml(commentout)
            }
          }]
          blocks = blocks.concat(nd_code_data);

          // commentout encode
          encode += DOMPurify.sanitize(marked(escapeHtml(commentout)))
          //  console.log(commentout)
        } else if (code_list[i].indexOf(document.getElementsByClassName("ace_comment")[commentoutnum].textContent) > -1){

          m = document.getElementsByClassName("ace_comment")[commentoutnum].textContent
          // Commentout 確認
          commentoutnum += 1;
          let commentout = "";
          // list -> string
          mutch_number += 1;
          //  m = String(code_list[i].match(regexp))
          let [a,b] = commentoutSystem(m,commentout)
          let lista = [a,b]
          m = lista[0];
          commentout = lista[1];
          // commentout encode
          encode += DOMPurify.sanitize(marked(escapeHtml(commentout)))
          //  console.log(commentout)
          code_list[i] = code_list[i].replace(m, "")
          codes(i, mutch_number)



        }else{
          codes(i, mutch_number)
        }
      } else {
        codes(i, mutch_number)
      }
    }
    //  console.log(encode)
    document.getElementById('article-show').innerHTML = encode
  }
