let Old_Scroll_Top = 0;
let Now_Scroll_Top = 0;

$(window).on('scroll',function(){
  Now_Scroll_Top = $(this).scrollTop();
    if (Now_Scroll_Top >= Old_Scroll_Top ) {
        $('.top_header').addClass('hidden');
    } else {
        $('.top_header').removeClass('hidden');
    }
    Old_Scroll_Top = Now_Scroll_Top;
});

// 初期設定
let show = "recentry-post";

function recentry_post() {
    if (show != "recentry-post"){
        document.getElementById(show).classList.remove('col-6');
        document.getElementById(show+"-content").classList.add('hide');
        document.getElementById("recentry-post-content").classList.remove('hide');
        document.getElementById(show).classList.add('col-2','section-not-choice');
        document.getElementById('recentry-post').classList.remove('col-2','section-not-choice');
        document.getElementById('recentry-post').classList.add('col-6');
        show = "recentry-post";
    }
}

function whole_post() {

    if (show != "whole-post"){
        document.getElementById(show).classList.remove('col-6');
        document.getElementById(show).classList.add('col-2','section-not-choice');
        document.getElementById(show+"-content").classList.add('hide');
        document.getElementById("whole-post-content").classList.remove('hide');
        document.getElementById('whole-post').classList.remove('col-2','section-not-choice');
        document.getElementById('whole-post').classList.add('col-6');
        show = "whole-post";
    }
}


function language_post() {

    if (show != "language-post"){
        document.getElementById(show).classList.remove('col-6');
        document.getElementById(show).classList.add('col-2','section-not-choice');
        document.getElementById('language-post').classList.remove('col-2','section-not-choice');
        document.getElementById('language-post').classList.add('col-6');
        document.getElementById(show+"-content").classList.add('hide');
        document.getElementById("language-post-content").classList.remove('hide');
        show = "language-post";
    }
}


function tag_post() {

    if (show != "tag-post"){
        document.getElementById(show).classList.remove('col-6');
        document.getElementById(show).classList.add('col-2','section-not-choice');
        document.getElementById('tag-post').classList.remove('col-2','section-not-choice');
        document.getElementById('tag-post').classList.add('col-6');
        document.getElementById(show+"-content").classList.add('hide');
        document.getElementById("tag-post-content").classList.remove('hide');
        show = "tag-post";
    }
}