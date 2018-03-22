```html
<!DOCTYPE html>
<html>
<head><meta charset="utf-8" />
<title>Traffic_Sign_Classifier</title><script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/require.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>

<style type="text/css">
    /*!
*
* Twitter Bootstrap
*
*/
/*!
 * Bootstrap v3.3.7 (http://getbootstrap.com)
 * Copyright 2011-2016 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE)
 */
/*! normalize.css v3.0.3 | MIT License | github.com/necolas/normalize.css */
html {
  font-family: sans-serif;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
}
body {
  margin: 0;
}
article,
aside,
details,
figcaption,
figure,
footer,
header,
hgroup,
main,
menu,
nav,
section,
summary {
  display: block;
}
audio,
canvas,
progress,
video {
  display: inline-block;
  vertical-align: baseline;
}
audio:not([controls]) {
  display: none;
  height: 0;
}
[hidden],
template {
  display: none;
}
a {
  background-color: transparent;
}
a:active,
a:hover {
  outline: 0;
}
abbr[title] {
  border-bottom: 1px dotted;
}
b,
strong {
  font-weight: bold;
}
dfn {
  font-style: italic;
}
h1 {
  font-size: 2em;
  margin: 0.67em 0;
}
mark {
  background: #ff0;
  color: #000;
}
small {
  font-size: 80%;
}
sub,
sup {
  font-size: 75%;
  line-height: 0;
  position: relative;
  vertical-align: baseline;
}
sup {
  top: -0.5em;
}
sub {
  bottom: -0.25em;
}
img {
  border: 0;
}
svg:not(:root) {
  overflow: hidden;
}
figure {
  margin: 1em 40px;
}
hr {
  box-sizing: content-box;
  height: 0;
}
pre {
  overflow: auto;
}
code,
kbd,
pre,
samp {
  font-family: monospace, monospace;
  font-size: 1em;
}
button,
input,
optgroup,
select,
textarea {
  color: inherit;
  font: inherit;
  margin: 0;
}
button {
  overflow: visible;
}
button,
select {
  text-transform: none;
}
button,
html input[type="button"],
input[type="reset"],
input[type="submit"] {
  -webkit-appearance: button;
  cursor: pointer;
}
button[disabled],
html input[disabled] {
  cursor: default;
}
button::-moz-focus-inner,
input::-moz-focus-inner {
  border: 0;
  padding: 0;
}
input {
  line-height: normal;
}
input[type="checkbox"],
input[type="radio"] {
  box-sizing: border-box;
  padding: 0;
}
input[type="number"]::-webkit-inner-spin-button,
input[type="number"]::-webkit-outer-spin-button {
  height: auto;
}
input[type="search"] {
  -webkit-appearance: textfield;
  box-sizing: content-box;
}
input[type="search"]::-webkit-search-cancel-button,
input[type="search"]::-webkit-search-decoration {
  -webkit-appearance: none;
}
fieldset {
  border: 1px solid #c0c0c0;
  margin: 0 2px;
  padding: 0.35em 0.625em 0.75em;
}
legend {
  border: 0;
  padding: 0;
}
textarea {
  overflow: auto;
}
optgroup {
  font-weight: bold;
}
table {
  border-collapse: collapse;
  border-spacing: 0;
}
td,
th {
  padding: 0;
}
/*! Source: https://github.com/h5bp/html5-boilerplate/blob/master/src/css/main.css */
@media print {
  *,
  *:before,
  *:after {
    background: transparent !important;
    color: #000 !important;
    box-shadow: none !important;
    text-shadow: none !important;
  }
  a,
  a:visited {
    text-decoration: underline;
  }
  a[href]:after {
    content: " (" attr(href) ")";
  }
  abbr[title]:after {
    content: " (" attr(title) ")";
  }
  a[href^="#"]:after,
  a[href^="javascript:"]:after {
    content: "";
  }
  pre,
  blockquote {
    border: 1px solid #999;
    page-break-inside: avoid;
  }
  thead {
    display: table-header-group;
  }
  tr,
  img {
    page-break-inside: avoid;
  }
  img {
    max-width: 100% !important;
  }
  p,
  h2,
  h3 {
    orphans: 3;
    widows: 3;
  }
  h2,
  h3 {
    page-break-after: avoid;
  }
  .navbar {
    display: none;
  }
  .btn > .caret,
  .dropup > .btn > .caret {
    border-top-color: #000 !important;
  }
  .label {
    border: 1px solid #000;
  }
  .table {
    border-collapse: collapse !important;
  }
  .table td,
  .table th {
    background-color: #fff !important;
  }
  .table-bordered th,
  .table-bordered td {
    border: 1px solid #ddd !important;
  }
}
@font-face {
  font-family: 'Glyphicons Halflings';
  src: url('../components/bootstrap/fonts/glyphicons-halflings-regular.eot');
  src: url('../components/bootstrap/fonts/glyphicons-halflings-regular.eot?#iefix') format('embedded-opentype'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.woff2') format('woff2'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.woff') format('woff'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.ttf') format('truetype'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.svg#glyphicons_halflingsregular') format('svg');
}
.glyphicon {
  position: relative;
  top: 1px;
  display: inline-block;
  font-family: 'Glyphicons Halflings';
  font-style: normal;
  font-weight: normal;
  line-height: 1;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
.glyphicon-asterisk:before {
  content: "\002a";
}
.glyphicon-plus:before {
  content: "\002b";
}
.glyphicon-euro:before,
.glyphicon-eur:before {
  content: "\20ac";
}
.glyphicon-minus:before {
  content: "\2212";
}
.glyphicon-cloud:before {
  content: "\2601";
}
.glyphicon-envelope:before {
  content: "\2709";
}
.glyphicon-pencil:before {
  content: "\270f";
}
.glyphicon-glass:before {
  content: "\e001";
}
.glyphicon-music:before {
  content: "\e002";
}
.glyphicon-search:before {
  content: "\e003";
}
.glyphicon-heart:before {
  content: "\e005";
}
.glyphicon-star:before {
  content: "\e006";
}
.glyphicon-star-empty:before {
  content: "\e007";
}
.glyphicon-user:before {
  content: "\e008";
}
.glyphicon-film:before {
  content: "\e009";
}
.glyphicon-th-large:before {
  content: "\e010";
}
.glyphicon-th:before {
  content: "\e011";
}
.glyphicon-th-list:before {
  content: "\e012";
}
.glyphicon-ok:before {
  content: "\e013";
}
.glyphicon-remove:before {
  content: "\e014";
}
.glyphicon-zoom-in:before {
  content: "\e015";
}
.glyphicon-zoom-out:before {
  content: "\e016";
}
.glyphicon-off:before {
  content: "\e017";
}
.glyphicon-signal:before {
  content: "\e018";
}
.glyphicon-cog:before {
  content: "\e019";
}
.glyphicon-trash:before {
  content: "\e020";
}
.glyphicon-home:before {
  content: "\e021";
}
.glyphicon-file:before {
  content: "\e022";
}
.glyphicon-time:before {
  content: "\e023";
}
.glyphicon-road:before {
  content: "\e024";
}
.glyphicon-download-alt:before {
  content: "\e025";
}
.glyphicon-download:before {
  content: "\e026";
}
.glyphicon-upload:before {
  content: "\e027";
}
.glyphicon-inbox:before {
  content: "\e028";
}
.glyphicon-play-circle:before {
  content: "\e029";
}
.glyphicon-repeat:before {
  content: "\e030";
}
.glyphicon-refresh:before {
  content: "\e031";
}
.glyphicon-list-alt:before {
  content: "\e032";
}
.glyphicon-lock:before {
  content: "\e033";
}
.glyphicon-flag:before {
  content: "\e034";
}
.glyphicon-headphones:before {
  content: "\e035";
}
.glyphicon-volume-off:before {
  content: "\e036";
}
.glyphicon-volume-down:before {
  content: "\e037";
}
.glyphicon-volume-up:before {
  content: "\e038";
}
.glyphicon-qrcode:before {
  content: "\e039";
}
.glyphicon-barcode:before {
  content: "\e040";
}
.glyphicon-tag:before {
  content: "\e041";
}
.glyphicon-tags:before {
  content: "\e042";
}
.glyphicon-book:before {
  content: "\e043";
}
.glyphicon-bookmark:before {
  content: "\e044";
}
.glyphicon-print:before {
  content: "\e045";
}
.glyphicon-camera:before {
  content: "\e046";
}
.glyphicon-font:before {
  content: "\e047";
}
.glyphicon-bold:before {
  content: "\e048";
}
.glyphicon-italic:before {
  content: "\e049";
}
.glyphicon-text-height:before {
  content: "\e050";
}
.glyphicon-text-width:before {
  content: "\e051";
}
.glyphicon-align-left:before {
  content: "\e052";
}
.glyphicon-align-center:before {
  content: "\e053";
}
.glyphicon-align-right:before {
  content: "\e054";
}
.glyphicon-align-justify:before {
  content: "\e055";
}
.glyphicon-list:before {
  content: "\e056";
}
.glyphicon-indent-left:before {
  content: "\e057";
}
.glyphicon-indent-right:before {
  content: "\e058";
}
.glyphicon-facetime-video:before {
  content: "\e059";
}
.glyphicon-picture:before {
  content: "\e060";
}
.glyphicon-map-marker:before {
  content: "\e062";
}
.glyphicon-adjust:before {
  content: "\e063";
}
.glyphicon-tint:before {
  content: "\e064";
}
.glyphicon-edit:before {
  content: "\e065";
}
.glyphicon-share:before {
  content: "\e066";
}
.glyphicon-check:before {
  content: "\e067";
}
.glyphicon-move:before {
  content: "\e068";
}
.glyphicon-step-backward:before {
  content: "\e069";
}
.glyphicon-fast-backward:before {
  content: "\e070";
}
.glyphicon-backward:before {
  content: "\e071";
}
.glyphicon-play:before {
  content: "\e072";
}
.glyphicon-pause:before {
  content: "\e073";
}
.glyphicon-stop:before {
  content: "\e074";
}
.glyphicon-forward:before {
  content: "\e075";
}
.glyphicon-fast-forward:before {
  content: "\e076";
}
.glyphicon-step-forward:before {
  content: "\e077";
}
.glyphicon-eject:before {
  content: "\e078";
}
.glyphicon-chevron-left:before {
  content: "\e079";
}
.glyphicon-chevron-right:before {
  content: "\e080";
}
.glyphicon-plus-sign:before {
  content: "\e081";
}
.glyphicon-minus-sign:before {
  content: "\e082";
}
.glyphicon-remove-sign:before {
  content: "\e083";
}
.glyphicon-ok-sign:before {
  content: "\e084";
}
.glyphicon-question-sign:before {
  content: "\e085";
}
.glyphicon-info-sign:before {
  content: "\e086";
}
.glyphicon-screenshot:before {
  content: "\e087";
}
.glyphicon-remove-circle:before {
  content: "\e088";
}
.glyphicon-ok-circle:before {
  content: "\e089";
}
.glyphicon-ban-circle:before {
  content: "\e090";
}
.glyphicon-arrow-left:before {
  content: "\e091";
}
.glyphicon-arrow-right:before {
  content: "\e092";
}
.glyphicon-arrow-up:before {
  content: "\e093";
}
.glyphicon-arrow-down:before {
  content: "\e094";
}
.glyphicon-share-alt:before {
  content: "\e095";
}
.glyphicon-resize-full:before {
  content: "\e096";
}
.glyphicon-resize-small:before {
  content: "\e097";
}
.glyphicon-exclamation-sign:before {
  content: "\e101";
}
.glyphicon-gift:before {
  content: "\e102";
}
.glyphicon-leaf:before {
  content: "\e103";
}
.glyphicon-fire:before {
  content: "\e104";
}
.glyphicon-eye-open:before {
  content: "\e105";
}
.glyphicon-eye-close:before {
  content: "\e106";
}
.glyphicon-warning-sign:before {
  content: "\e107";
}
.glyphicon-plane:before {
  content: "\e108";
}
.glyphicon-calendar:before {
  content: "\e109";
}
.glyphicon-random:before {
  content: "\e110";
}
.glyphicon-comment:before {
  content: "\e111";
}
.glyphicon-magnet:before {
  content: "\e112";
}
.glyphicon-chevron-up:before {
  content: "\e113";
}
.glyphicon-chevron-down:before {
  content: "\e114";
}
.glyphicon-retweet:before {
  content: "\e115";
}
.glyphicon-shopping-cart:before {
  content: "\e116";
}
.glyphicon-folder-close:before {
  content: "\e117";
}
.glyphicon-folder-open:before {
  content: "\e118";
}
.glyphicon-resize-vertical:before {
  content: "\e119";
}
.glyphicon-resize-horizontal:before {
  content: "\e120";
}
.glyphicon-hdd:before {
  content: "\e121";
}
.glyphicon-bullhorn:before {
  content: "\e122";
}
.glyphicon-bell:before {
  content: "\e123";
}
.glyphicon-certificate:before {
  content: "\e124";
}
.glyphicon-thumbs-up:before {
  content: "\e125";
}
.glyphicon-thumbs-down:before {
  content: "\e126";
}
.glyphicon-hand-right:before {
  content: "\e127";
}
.glyphicon-hand-left:before {
  content: "\e128";
}
.glyphicon-hand-up:before {
  content: "\e129";
}
.glyphicon-hand-down:before {
  content: "\e130";
}
.glyphicon-circle-arrow-right:before {
  content: "\e131";
}
.glyphicon-circle-arrow-left:before {
  content: "\e132";
}
.glyphicon-circle-arrow-up:before {
  content: "\e133";
}
.glyphicon-circle-arrow-down:before {
  content: "\e134";
}
.glyphicon-globe:before {
  content: "\e135";
}
.glyphicon-wrench:before {
  content: "\e136";
}
.glyphicon-tasks:before {
  content: "\e137";
}
.glyphicon-filter:before {
  content: "\e138";
}
.glyphicon-briefcase:before {
  content: "\e139";
}
.glyphicon-fullscreen:before {
  content: "\e140";
}
.glyphicon-dashboard:before {
  content: "\e141";
}
.glyphicon-paperclip:before {
  content: "\e142";
}
.glyphicon-heart-empty:before {
  content: "\e143";
}
.glyphicon-link:before {
  content: "\e144";
}
.glyphicon-phone:before {
  content: "\e145";
}
.glyphicon-pushpin:before {
  content: "\e146";
}
.glyphicon-usd:before {
  content: "\e148";
}
.glyphicon-gbp:before {
  content: "\e149";
}
.glyphicon-sort:before {
  content: "\e150";
}
.glyphicon-sort-by-alphabet:before {
  content: "\e151";
}
.glyphicon-sort-by-alphabet-alt:before {
  content: "\e152";
}
.glyphicon-sort-by-order:before {
  content: "\e153";
}
.glyphicon-sort-by-order-alt:before {
  content: "\e154";
}
.glyphicon-sort-by-attributes:before {
  content: "\e155";
}
.glyphicon-sort-by-attributes-alt:before {
  content: "\e156";
}
.glyphicon-unchecked:before {
  content: "\e157";
}
.glyphicon-expand:before {
  content: "\e158";
}
.glyphicon-collapse-down:before {
  content: "\e159";
}
.glyphicon-collapse-up:before {
  content: "\e160";
}
.glyphicon-log-in:before {
  content: "\e161";
}
.glyphicon-flash:before {
  content: "\e162";
}
.glyphicon-log-out:before {
  content: "\e163";
}
.glyphicon-new-window:before {
  content: "\e164";
}
.glyphicon-record:before {
  content: "\e165";
}
.glyphicon-save:before {
  content: "\e166";
}
.glyphicon-open:before {
  content: "\e167";
}
.glyphicon-saved:before {
  content: "\e168";
}
.glyphicon-import:before {
  content: "\e169";
}
.glyphicon-export:before {
  content: "\e170";
}
.glyphicon-send:before {
  content: "\e171";
}
.glyphicon-floppy-disk:before {
  content: "\e172";
}
.glyphicon-floppy-saved:before {
  content: "\e173";
}
.glyphicon-floppy-remove:before {
  content: "\e174";
}
.glyphicon-floppy-save:before {
  content: "\e175";
}
.glyphicon-floppy-open:before {
  content: "\e176";
}
.glyphicon-credit-card:before {
  content: "\e177";
}
.glyphicon-transfer:before {
  content: "\e178";
}
.glyphicon-cutlery:before {
  content: "\e179";
}
.glyphicon-header:before {
  content: "\e180";
}
.glyphicon-compressed:before {
  content: "\e181";
}
.glyphicon-earphone:before {
  content: "\e182";
}
.glyphicon-phone-alt:before {
  content: "\e183";
}
.glyphicon-tower:before {
  content: "\e184";
}
.glyphicon-stats:before {
  content: "\e185";
}
.glyphicon-sd-video:before {
  content: "\e186";
}
.glyphicon-hd-video:before {
  content: "\e187";
}
.glyphicon-subtitles:before {
  content: "\e188";
}
.glyphicon-sound-stereo:before {
  content: "\e189";
}
.glyphicon-sound-dolby:before {
  content: "\e190";
}
.glyphicon-sound-5-1:before {
  content: "\e191";
}
.glyphicon-sound-6-1:before {
  content: "\e192";
}
.glyphicon-sound-7-1:before {
  content: "\e193";
}
.glyphicon-copyright-mark:before {
  content: "\e194";
}
.glyphicon-registration-mark:before {
  content: "\e195";
}
.glyphicon-cloud-download:before {
  content: "\e197";
}
.glyphicon-cloud-upload:before {
  content: "\e198";
}
.glyphicon-tree-conifer:before {
  content: "\e199";
}
.glyphicon-tree-deciduous:before {
  content: "\e200";
}
.glyphicon-cd:before {
  content: "\e201";
}
.glyphicon-save-file:before {
  content: "\e202";
}
.glyphicon-open-file:before {
  content: "\e203";
}
.glyphicon-level-up:before {
  content: "\e204";
}
.glyphicon-copy:before {
  content: "\e205";
}
.glyphicon-paste:before {
  content: "\e206";
}
.glyphicon-alert:before {
  content: "\e209";
}
.glyphicon-equalizer:before {
  content: "\e210";
}
.glyphicon-king:before {
  content: "\e211";
}
.glyphicon-queen:before {
  content: "\e212";
}
.glyphicon-pawn:before {
  content: "\e213";
}
.glyphicon-bishop:before {
  content: "\e214";
}
.glyphicon-knight:before {
  content: "\e215";
}
.glyphicon-baby-formula:before {
  content: "\e216";
}
.glyphicon-tent:before {
  content: "\26fa";
}
.glyphicon-blackboard:before {
  content: "\e218";
}
.glyphicon-bed:before {
  content: "\e219";
}
.glyphicon-apple:before {
  content: "\f8ff";
}
.glyphicon-erase:before {
  content: "\e221";
}
.glyphicon-hourglass:before {
  content: "\231b";
}
.glyphicon-lamp:before {
  content: "\e223";
}
.glyphicon-duplicate:before {
  content: "\e224";
}
.glyphicon-piggy-bank:before {
  content: "\e225";
}
.glyphicon-scissors:before {
  content: "\e226";
}
.glyphicon-bitcoin:before {
  content: "\e227";
}
.glyphicon-btc:before {
  content: "\e227";
}
.glyphicon-xbt:before {
  content: "\e227";
}
.glyphicon-yen:before {
  content: "\00a5";
}
.glyphicon-jpy:before {
  content: "\00a5";
}
.glyphicon-ruble:before {
  content: "\20bd";
}
.glyphicon-rub:before {
  content: "\20bd";
}
.glyphicon-scale:before {
  content: "\e230";
}
.glyphicon-ice-lolly:before {
  content: "\e231";
}
.glyphicon-ice-lolly-tasted:before {
  content: "\e232";
}
.glyphicon-education:before {
  content: "\e233";
}
.glyphicon-option-horizontal:before {
  content: "\e234";
}
.glyphicon-option-vertical:before {
  content: "\e235";
}
.glyphicon-menu-hamburger:before {
  content: "\e236";
}
.glyphicon-modal-window:before {
  content: "\e237";
}
.glyphicon-oil:before {
  content: "\e238";
}
.glyphicon-grain:before {
  content: "\e239";
}
.glyphicon-sunglasses:before {
  content: "\e240";
}
.glyphicon-text-size:before {
  content: "\e241";
}
.glyphicon-text-color:before {
  content: "\e242";
}
.glyphicon-text-background:before {
  content: "\e243";
}
.glyphicon-object-align-top:before {
  content: "\e244";
}
.glyphicon-object-align-bottom:before {
  content: "\e245";
}
.glyphicon-object-align-horizontal:before {
  content: "\e246";
}
.glyphicon-object-align-left:before {
  content: "\e247";
}
.glyphicon-object-align-vertical:before {
  content: "\e248";
}
.glyphicon-object-align-right:before {
  content: "\e249";
}
.glyphicon-triangle-right:before {
  content: "\e250";
}
.glyphicon-triangle-left:before {
  content: "\e251";
}
.glyphicon-triangle-bottom:before {
  content: "\e252";
}
.glyphicon-triangle-top:before {
  content: "\e253";
}
.glyphicon-console:before {
  content: "\e254";
}
.glyphicon-superscript:before {
  content: "\e255";
}
.glyphicon-subscript:before {
  content: "\e256";
}
.glyphicon-menu-left:before {
  content: "\e257";
}
.glyphicon-menu-right:before {
  content: "\e258";
}
.glyphicon-menu-down:before {
  content: "\e259";
}
.glyphicon-menu-up:before {
  content: "\e260";
}
* {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
*:before,
*:after {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
html {
  font-size: 10px;
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
}
body {
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 13px;
  line-height: 1.42857143;
  color: #000;
  background-color: #fff;
}
input,
button,
select,
textarea {
  font-family: inherit;
  font-size: inherit;
  line-height: inherit;
}
a {
  color: #337ab7;
  text-decoration: none;
}
a:hover,
a:focus {
  color: #23527c;
  text-decoration: underline;
}
a:focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
figure {
  margin: 0;
}
img {
  vertical-align: middle;
}
.img-responsive,
.thumbnail > img,
.thumbnail a > img,
.carousel-inner > .item > img,
.carousel-inner > .item > a > img {
  display: block;
  max-width: 100%;
  height: auto;
}
.img-rounded {
  border-radius: 3px;
}
.img-thumbnail {
  padding: 4px;
  line-height: 1.42857143;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 2px;
  -webkit-transition: all 0.2s ease-in-out;
  -o-transition: all 0.2s ease-in-out;
  transition: all 0.2s ease-in-out;
  display: inline-block;
  max-width: 100%;
  height: auto;
}
.img-circle {
  border-radius: 50%;
}
hr {
  margin-top: 18px;
  margin-bottom: 18px;
  border: 0;
  border-top: 1px solid #eeeeee;
}
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
[role="button"] {
  cursor: pointer;
}
h1,
h2,
h3,
h4,
h5,
h6,
.h1,
.h2,
.h3,
.h4,
.h5,
.h6 {
  font-family: inherit;
  font-weight: 500;
  line-height: 1.1;
  color: inherit;
}
h1 small,
h2 small,
h3 small,
h4 small,
h5 small,
h6 small,
.h1 small,
.h2 small,
.h3 small,
.h4 small,
.h5 small,
.h6 small,
h1 .small,
h2 .small,
h3 .small,
h4 .small,
h5 .small,
h6 .small,
.h1 .small,
.h2 .small,
.h3 .small,
.h4 .small,
.h5 .small,
.h6 .small {
  font-weight: normal;
  line-height: 1;
  color: #777777;
}
h1,
.h1,
h2,
.h2,
h3,
.h3 {
  margin-top: 18px;
  margin-bottom: 9px;
}
h1 small,
.h1 small,
h2 small,
.h2 small,
h3 small,
.h3 small,
h1 .small,
.h1 .small,
h2 .small,
.h2 .small,
h3 .small,
.h3 .small {
  font-size: 65%;
}
h4,
.h4,
h5,
.h5,
h6,
.h6 {
  margin-top: 9px;
  margin-bottom: 9px;
}
h4 small,
.h4 small,
h5 small,
.h5 small,
h6 small,
.h6 small,
h4 .small,
.h4 .small,
h5 .small,
.h5 .small,
h6 .small,
.h6 .small {
  font-size: 75%;
}
h1,
.h1 {
  font-size: 33px;
}
h2,
.h2 {
  font-size: 27px;
}
h3,
.h3 {
  font-size: 23px;
}
h4,
.h4 {
  font-size: 17px;
}
h5,
.h5 {
  font-size: 13px;
}
h6,
.h6 {
  font-size: 12px;
}
p {
  margin: 0 0 9px;
}
.lead {
  margin-bottom: 18px;
  font-size: 14px;
  font-weight: 300;
  line-height: 1.4;
}
@media (min-width: 768px) {
  .lead {
    font-size: 19.5px;
  }
}
small,
.small {
  font-size: 92%;
}
mark,
.mark {
  background-color: #fcf8e3;
  padding: .2em;
}
.text-left {
  text-align: left;
}
.text-right {
  text-align: right;
}
.text-center {
  text-align: center;
}
.text-justify {
  text-align: justify;
}
.text-nowrap {
  white-space: nowrap;
}
.text-lowercase {
  text-transform: lowercase;
}
.text-uppercase {
  text-transform: uppercase;
}
.text-capitalize {
  text-transform: capitalize;
}
.text-muted {
  color: #777777;
}
.text-primary {
  color: #337ab7;
}
a.text-primary:hover,
a.text-primary:focus {
  color: #286090;
}
.text-success {
  color: #3c763d;
}
a.text-success:hover,
a.text-success:focus {
  color: #2b542c;
}
.text-info {
  color: #31708f;
}
a.text-info:hover,
a.text-info:focus {
  color: #245269;
}
.text-warning {
  color: #8a6d3b;
}
a.text-warning:hover,
a.text-warning:focus {
  color: #66512c;
}
.text-danger {
  color: #a94442;
}
a.text-danger:hover,
a.text-danger:focus {
  color: #843534;
}
.bg-primary {
  color: #fff;
  background-color: #337ab7;
}
a.bg-primary:hover,
a.bg-primary:focus {
  background-color: #286090;
}
.bg-success {
  background-color: #dff0d8;
}
a.bg-success:hover,
a.bg-success:focus {
  background-color: #c1e2b3;
}
.bg-info {
  background-color: #d9edf7;
}
a.bg-info:hover,
a.bg-info:focus {
  background-color: #afd9ee;
}
.bg-warning {
  background-color: #fcf8e3;
}
a.bg-warning:hover,
a.bg-warning:focus {
  background-color: #f7ecb5;
}
.bg-danger {
  background-color: #f2dede;
}
a.bg-danger:hover,
a.bg-danger:focus {
  background-color: #e4b9b9;
}
.page-header {
  padding-bottom: 8px;
  margin: 36px 0 18px;
  border-bottom: 1px solid #eeeeee;
}
ul,
ol {
  margin-top: 0;
  margin-bottom: 9px;
}
ul ul,
ol ul,
ul ol,
ol ol {
  margin-bottom: 0;
}
.list-unstyled {
  padding-left: 0;
  list-style: none;
}
.list-inline {
  padding-left: 0;
  list-style: none;
  margin-left: -5px;
}
.list-inline > li {
  display: inline-block;
  padding-left: 5px;
  padding-right: 5px;
}
dl {
  margin-top: 0;
  margin-bottom: 18px;
}
dt,
dd {
  line-height: 1.42857143;
}
dt {
  font-weight: bold;
}
dd {
  margin-left: 0;
}
@media (min-width: 541px) {
  .dl-horizontal dt {
    float: left;
    width: 160px;
    clear: left;
    text-align: right;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }
  .dl-horizontal dd {
    margin-left: 180px;
  }
}
abbr[title],
abbr[data-original-title] {
  cursor: help;
  border-bottom: 1px dotted #777777;
}
.initialism {
  font-size: 90%;
  text-transform: uppercase;
}
blockquote {
  padding: 9px 18px;
  margin: 0 0 18px;
  font-size: inherit;
  border-left: 5px solid #eeeeee;
}
blockquote p:last-child,
blockquote ul:last-child,
blockquote ol:last-child {
  margin-bottom: 0;
}
blockquote footer,
blockquote small,
blockquote .small {
  display: block;
  font-size: 80%;
  line-height: 1.42857143;
  color: #777777;
}
blockquote footer:before,
blockquote small:before,
blockquote .small:before {
  content: '\2014 \00A0';
}
.blockquote-reverse,
blockquote.pull-right {
  padding-right: 15px;
  padding-left: 0;
  border-right: 5px solid #eeeeee;
  border-left: 0;
  text-align: right;
}
.blockquote-reverse footer:before,
blockquote.pull-right footer:before,
.blockquote-reverse small:before,
blockquote.pull-right small:before,
.blockquote-reverse .small:before,
blockquote.pull-right .small:before {
  content: '';
}
.blockquote-reverse footer:after,
blockquote.pull-right footer:after,
.blockquote-reverse small:after,
blockquote.pull-right small:after,
.blockquote-reverse .small:after,
blockquote.pull-right .small:after {
  content: '\00A0 \2014';
}
address {
  margin-bottom: 18px;
  font-style: normal;
  line-height: 1.42857143;
}
code,
kbd,
pre,
samp {
  font-family: monospace;
}
code {
  padding: 2px 4px;
  font-size: 90%;
  color: #c7254e;
  background-color: #f9f2f4;
  border-radius: 2px;
}
kbd {
  padding: 2px 4px;
  font-size: 90%;
  color: #888;
  background-color: transparent;
  border-radius: 1px;
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.25);
}
kbd kbd {
  padding: 0;
  font-size: 100%;
  font-weight: bold;
  box-shadow: none;
}
pre {
  display: block;
  padding: 8.5px;
  margin: 0 0 9px;
  font-size: 12px;
  line-height: 1.42857143;
  word-break: break-all;
  word-wrap: break-word;
  color: #333333;
  background-color: #f5f5f5;
  border: 1px solid #ccc;
  border-radius: 2px;
}
pre code {
  padding: 0;
  font-size: inherit;
  color: inherit;
  white-space: pre-wrap;
  background-color: transparent;
  border-radius: 0;
}
.pre-scrollable {
  max-height: 340px;
  overflow-y: scroll;
}
.container {
  margin-right: auto;
  margin-left: auto;
  padding-left: 0px;
  padding-right: 0px;
}
@media (min-width: 768px) {
  .container {
    width: 768px;
  }
}
@media (min-width: 992px) {
  .container {
    width: 940px;
  }
}
@media (min-width: 1200px) {
  .container {
    width: 1140px;
  }
}
.container-fluid {
  margin-right: auto;
  margin-left: auto;
  padding-left: 0px;
  padding-right: 0px;
}
.row {
  margin-left: 0px;
  margin-right: 0px;
}
.col-xs-1, .col-sm-1, .col-md-1, .col-lg-1, .col-xs-2, .col-sm-2, .col-md-2, .col-lg-2, .col-xs-3, .col-sm-3, .col-md-3, .col-lg-3, .col-xs-4, .col-sm-4, .col-md-4, .col-lg-4, .col-xs-5, .col-sm-5, .col-md-5, .col-lg-5, .col-xs-6, .col-sm-6, .col-md-6, .col-lg-6, .col-xs-7, .col-sm-7, .col-md-7, .col-lg-7, .col-xs-8, .col-sm-8, .col-md-8, .col-lg-8, .col-xs-9, .col-sm-9, .col-md-9, .col-lg-9, .col-xs-10, .col-sm-10, .col-md-10, .col-lg-10, .col-xs-11, .col-sm-11, .col-md-11, .col-lg-11, .col-xs-12, .col-sm-12, .col-md-12, .col-lg-12 {
  position: relative;
  min-height: 1px;
  padding-left: 0px;
  padding-right: 0px;
}
.col-xs-1, .col-xs-2, .col-xs-3, .col-xs-4, .col-xs-5, .col-xs-6, .col-xs-7, .col-xs-8, .col-xs-9, .col-xs-10, .col-xs-11, .col-xs-12 {
  float: left;
}
.col-xs-12 {
  width: 100%;
}
.col-xs-11 {
  width: 91.66666667%;
}
.col-xs-10 {
  width: 83.33333333%;
}
.col-xs-9 {
  width: 75%;
}
.col-xs-8 {
  width: 66.66666667%;
}
.col-xs-7 {
  width: 58.33333333%;
}
.col-xs-6 {
  width: 50%;
}
.col-xs-5 {
  width: 41.66666667%;
}
.col-xs-4 {
  width: 33.33333333%;
}
.col-xs-3 {
  width: 25%;
}
.col-xs-2 {
  width: 16.66666667%;
}
.col-xs-1 {
  width: 8.33333333%;
}
.col-xs-pull-12 {
  right: 100%;
}
.col-xs-pull-11 {
  right: 91.66666667%;
}
.col-xs-pull-10 {
  right: 83.33333333%;
}
.col-xs-pull-9 {
  right: 75%;
}
.col-xs-pull-8 {
  right: 66.66666667%;
}
.col-xs-pull-7 {
  right: 58.33333333%;
}
.col-xs-pull-6 {
  right: 50%;
}
.col-xs-pull-5 {
  right: 41.66666667%;
}
.col-xs-pull-4 {
  right: 33.33333333%;
}
.col-xs-pull-3 {
  right: 25%;
}
.col-xs-pull-2 {
  right: 16.66666667%;
}
.col-xs-pull-1 {
  right: 8.33333333%;
}
.col-xs-pull-0 {
  right: auto;
}
.col-xs-push-12 {
  left: 100%;
}
.col-xs-push-11 {
  left: 91.66666667%;
}
.col-xs-push-10 {
  left: 83.33333333%;
}
.col-xs-push-9 {
  left: 75%;
}
.col-xs-push-8 {
  left: 66.66666667%;
}
.col-xs-push-7 {
  left: 58.33333333%;
}
.col-xs-push-6 {
  left: 50%;
}
.col-xs-push-5 {
  left: 41.66666667%;
}
.col-xs-push-4 {
  left: 33.33333333%;
}
.col-xs-push-3 {
  left: 25%;
}
.col-xs-push-2 {
  left: 16.66666667%;
}
.col-xs-push-1 {
  left: 8.33333333%;
}
.col-xs-push-0 {
  left: auto;
}
.col-xs-offset-12 {
  margin-left: 100%;
}
.col-xs-offset-11 {
  margin-left: 91.66666667%;
}
.col-xs-offset-10 {
  margin-left: 83.33333333%;
}
.col-xs-offset-9 {
  margin-left: 75%;
}
.col-xs-offset-8 {
  margin-left: 66.66666667%;
}
.col-xs-offset-7 {
  margin-left: 58.33333333%;
}
.col-xs-offset-6 {
  margin-left: 50%;
}
.col-xs-offset-5 {
  margin-left: 41.66666667%;
}
.col-xs-offset-4 {
  margin-left: 33.33333333%;
}
.col-xs-offset-3 {
  margin-left: 25%;
}
.col-xs-offset-2 {
  margin-left: 16.66666667%;
}
.col-xs-offset-1 {
  margin-left: 8.33333333%;
}
.col-xs-offset-0 {
  margin-left: 0%;
}
@media (min-width: 768px) {
  .col-sm-1, .col-sm-2, .col-sm-3, .col-sm-4, .col-sm-5, .col-sm-6, .col-sm-7, .col-sm-8, .col-sm-9, .col-sm-10, .col-sm-11, .col-sm-12 {
    float: left;
  }
  .col-sm-12 {
    width: 100%;
  }
  .col-sm-11 {
    width: 91.66666667%;
  }
  .col-sm-10 {
    width: 83.33333333%;
  }
  .col-sm-9 {
    width: 75%;
  }
  .col-sm-8 {
    width: 66.66666667%;
  }
  .col-sm-7 {
    width: 58.33333333%;
  }
  .col-sm-6 {
    width: 50%;
  }
  .col-sm-5 {
    width: 41.66666667%;
  }
  .col-sm-4 {
    width: 33.33333333%;
  }
  .col-sm-3 {
    width: 25%;
  }
  .col-sm-2 {
    width: 16.66666667%;
  }
  .col-sm-1 {
    width: 8.33333333%;
  }
  .col-sm-pull-12 {
    right: 100%;
  }
  .col-sm-pull-11 {
    right: 91.66666667%;
  }
  .col-sm-pull-10 {
    right: 83.33333333%;
  }
  .col-sm-pull-9 {
    right: 75%;
  }
  .col-sm-pull-8 {
    right: 66.66666667%;
  }
  .col-sm-pull-7 {
    right: 58.33333333%;
  }
  .col-sm-pull-6 {
    right: 50%;
  }
  .col-sm-pull-5 {
    right: 41.66666667%;
  }
  .col-sm-pull-4 {
    right: 33.33333333%;
  }
  .col-sm-pull-3 {
    right: 25%;
  }
  .col-sm-pull-2 {
    right: 16.66666667%;
  }
  .col-sm-pull-1 {
    right: 8.33333333%;
  }
  .col-sm-pull-0 {
    right: auto;
  }
  .col-sm-push-12 {
    left: 100%;
  }
  .col-sm-push-11 {
    left: 91.66666667%;
  }
  .col-sm-push-10 {
    left: 83.33333333%;
  }
  .col-sm-push-9 {
    left: 75%;
  }
  .col-sm-push-8 {
    left: 66.66666667%;
  }
  .col-sm-push-7 {
    left: 58.33333333%;
  }
  .col-sm-push-6 {
    left: 50%;
  }
  .col-sm-push-5 {
    left: 41.66666667%;
  }
  .col-sm-push-4 {
    left: 33.33333333%;
  }
  .col-sm-push-3 {
    left: 25%;
  }
  .col-sm-push-2 {
    left: 16.66666667%;
  }
  .col-sm-push-1 {
    left: 8.33333333%;
  }
  .col-sm-push-0 {
    left: auto;
  }
  .col-sm-offset-12 {
    margin-left: 100%;
  }
  .col-sm-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-sm-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-sm-offset-9 {
    margin-left: 75%;
  }
  .col-sm-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-sm-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-sm-offset-6 {
    margin-left: 50%;
  }
  .col-sm-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-sm-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-sm-offset-3 {
    margin-left: 25%;
  }
  .col-sm-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-sm-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-sm-offset-0 {
    margin-left: 0%;
  }
}
@media (min-width: 992px) {
  .col-md-1, .col-md-2, .col-md-3, .col-md-4, .col-md-5, .col-md-6, .col-md-7, .col-md-8, .col-md-9, .col-md-10, .col-md-11, .col-md-12 {
    float: left;
  }
  .col-md-12 {
    width: 100%;
  }
  .col-md-11 {
    width: 91.66666667%;
  }
  .col-md-10 {
    width: 83.33333333%;
  }
  .col-md-9 {
    width: 75%;
  }
  .col-md-8 {
    width: 66.66666667%;
  }
  .col-md-7 {
    width: 58.33333333%;
  }
  .col-md-6 {
    width: 50%;
  }
  .col-md-5 {
    width: 41.66666667%;
  }
  .col-md-4 {
    width: 33.33333333%;
  }
  .col-md-3 {
    width: 25%;
  }
  .col-md-2 {
    width: 16.66666667%;
  }
  .col-md-1 {
    width: 8.33333333%;
  }
  .col-md-pull-12 {
    right: 100%;
  }
  .col-md-pull-11 {
    right: 91.66666667%;
  }
  .col-md-pull-10 {
    right: 83.33333333%;
  }
  .col-md-pull-9 {
    right: 75%;
  }
  .col-md-pull-8 {
    right: 66.66666667%;
  }
  .col-md-pull-7 {
    right: 58.33333333%;
  }
  .col-md-pull-6 {
    right: 50%;
  }
  .col-md-pull-5 {
    right: 41.66666667%;
  }
  .col-md-pull-4 {
    right: 33.33333333%;
  }
  .col-md-pull-3 {
    right: 25%;
  }
  .col-md-pull-2 {
    right: 16.66666667%;
  }
  .col-md-pull-1 {
    right: 8.33333333%;
  }
  .col-md-pull-0 {
    right: auto;
  }
  .col-md-push-12 {
    left: 100%;
  }
  .col-md-push-11 {
    left: 91.66666667%;
  }
  .col-md-push-10 {
    left: 83.33333333%;
  }
  .col-md-push-9 {
    left: 75%;
  }
  .col-md-push-8 {
    left: 66.66666667%;
  }
  .col-md-push-7 {
    left: 58.33333333%;
  }
  .col-md-push-6 {
    left: 50%;
  }
  .col-md-push-5 {
    left: 41.66666667%;
  }
  .col-md-push-4 {
    left: 33.33333333%;
  }
  .col-md-push-3 {
    left: 25%;
  }
  .col-md-push-2 {
    left: 16.66666667%;
  }
  .col-md-push-1 {
    left: 8.33333333%;
  }
  .col-md-push-0 {
    left: auto;
  }
  .col-md-offset-12 {
    margin-left: 100%;
  }
  .col-md-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-md-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-md-offset-9 {
    margin-left: 75%;
  }
  .col-md-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-md-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-md-offset-6 {
    margin-left: 50%;
  }
  .col-md-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-md-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-md-offset-3 {
    margin-left: 25%;
  }
  .col-md-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-md-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-md-offset-0 {
    margin-left: 0%;
  }
}
@media (min-width: 1200px) {
  .col-lg-1, .col-lg-2, .col-lg-3, .col-lg-4, .col-lg-5, .col-lg-6, .col-lg-7, .col-lg-8, .col-lg-9, .col-lg-10, .col-lg-11, .col-lg-12 {
    float: left;
  }
  .col-lg-12 {
    width: 100%;
  }
  .col-lg-11 {
    width: 91.66666667%;
  }
  .col-lg-10 {
    width: 83.33333333%;
  }
  .col-lg-9 {
    width: 75%;
  }
  .col-lg-8 {
    width: 66.66666667%;
  }
  .col-lg-7 {
    width: 58.33333333%;
  }
  .col-lg-6 {
    width: 50%;
  }
  .col-lg-5 {
    width: 41.66666667%;
  }
  .col-lg-4 {
    width: 33.33333333%;
  }
  .col-lg-3 {
    width: 25%;
  }
  .col-lg-2 {
    width: 16.66666667%;
  }
  .col-lg-1 {
    width: 8.33333333%;
  }
  .col-lg-pull-12 {
    right: 100%;
  }
  .col-lg-pull-11 {
    right: 91.66666667%;
  }
  .col-lg-pull-10 {
    right: 83.33333333%;
  }
  .col-lg-pull-9 {
    right: 75%;
  }
  .col-lg-pull-8 {
    right: 66.66666667%;
  }
  .col-lg-pull-7 {
    right: 58.33333333%;
  }
  .col-lg-pull-6 {
    right: 50%;
  }
  .col-lg-pull-5 {
    right: 41.66666667%;
  }
  .col-lg-pull-4 {
    right: 33.33333333%;
  }
  .col-lg-pull-3 {
    right: 25%;
  }
  .col-lg-pull-2 {
    right: 16.66666667%;
  }
  .col-lg-pull-1 {
    right: 8.33333333%;
  }
  .col-lg-pull-0 {
    right: auto;
  }
  .col-lg-push-12 {
    left: 100%;
  }
  .col-lg-push-11 {
    left: 91.66666667%;
  }
  .col-lg-push-10 {
    left: 83.33333333%;
  }
  .col-lg-push-9 {
    left: 75%;
  }
  .col-lg-push-8 {
    left: 66.66666667%;
  }
  .col-lg-push-7 {
    left: 58.33333333%;
  }
  .col-lg-push-6 {
    left: 50%;
  }
  .col-lg-push-5 {
    left: 41.66666667%;
  }
  .col-lg-push-4 {
    left: 33.33333333%;
  }
  .col-lg-push-3 {
    left: 25%;
  }
  .col-lg-push-2 {
    left: 16.66666667%;
  }
  .col-lg-push-1 {
    left: 8.33333333%;
  }
  .col-lg-push-0 {
    left: auto;
  }
  .col-lg-offset-12 {
    margin-left: 100%;
  }
  .col-lg-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-lg-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-lg-offset-9 {
    margin-left: 75%;
  }
  .col-lg-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-lg-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-lg-offset-6 {
    margin-left: 50%;
  }
  .col-lg-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-lg-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-lg-offset-3 {
    margin-left: 25%;
  }
  .col-lg-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-lg-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-lg-offset-0 {
    margin-left: 0%;
  }
}
table {
  background-color: transparent;
}
caption {
  padding-top: 8px;
  padding-bottom: 8px;
  color: #777777;
  text-align: left;
}
th {
  text-align: left;
}
.table {
  width: 100%;
  max-width: 100%;
  margin-bottom: 18px;
}
.table > thead > tr > th,
.table > tbody > tr > th,
.table > tfoot > tr > th,
.table > thead > tr > td,
.table > tbody > tr > td,
.table > tfoot > tr > td {
  padding: 8px;
  line-height: 1.42857143;
  vertical-align: top;
  border-top: 1px solid #ddd;
}
.table > thead > tr > th {
  vertical-align: bottom;
  border-bottom: 2px solid #ddd;
}
.table > caption + thead > tr:first-child > th,
.table > colgroup + thead > tr:first-child > th,
.table > thead:first-child > tr:first-child > th,
.table > caption + thead > tr:first-child > td,
.table > colgroup + thead > tr:first-child > td,
.table > thead:first-child > tr:first-child > td {
  border-top: 0;
}
.table > tbody + tbody {
  border-top: 2px solid #ddd;
}
.table .table {
  background-color: #fff;
}
.table-condensed > thead > tr > th,
.table-condensed > tbody > tr > th,
.table-condensed > tfoot > tr > th,
.table-condensed > thead > tr > td,
.table-condensed > tbody > tr > td,
.table-condensed > tfoot > tr > td {
  padding: 5px;
}
.table-bordered {
  border: 1px solid #ddd;
}
.table-bordered > thead > tr > th,
.table-bordered > tbody > tr > th,
.table-bordered > tfoot > tr > th,
.table-bordered > thead > tr > td,
.table-bordered > tbody > tr > td,
.table-bordered > tfoot > tr > td {
  border: 1px solid #ddd;
}
.table-bordered > thead > tr > th,
.table-bordered > thead > tr > td {
  border-bottom-width: 2px;
}
.table-striped > tbody > tr:nth-of-type(odd) {
  background-color: #f9f9f9;
}
.table-hover > tbody > tr:hover {
  background-color: #f5f5f5;
}
table col[class*="col-"] {
  position: static;
  float: none;
  display: table-column;
}
table td[class*="col-"],
table th[class*="col-"] {
  position: static;
  float: none;
  display: table-cell;
}
.table > thead > tr > td.active,
.table > tbody > tr > td.active,
.table > tfoot > tr > td.active,
.table > thead > tr > th.active,
.table > tbody > tr > th.active,
.table > tfoot > tr > th.active,
.table > thead > tr.active > td,
.table > tbody > tr.active > td,
.table > tfoot > tr.active > td,
.table > thead > tr.active > th,
.table > tbody > tr.active > th,
.table > tfoot > tr.active > th {
  background-color: #f5f5f5;
}
.table-hover > tbody > tr > td.active:hover,
.table-hover > tbody > tr > th.active:hover,
.table-hover > tbody > tr.active:hover > td,
.table-hover > tbody > tr:hover > .active,
.table-hover > tbody > tr.active:hover > th {
  background-color: #e8e8e8;
}
.table > thead > tr > td.success,
.table > tbody > tr > td.success,
.table > tfoot > tr > td.success,
.table > thead > tr > th.success,
.table > tbody > tr > th.success,
.table > tfoot > tr > th.success,
.table > thead > tr.success > td,
.table > tbody > tr.success > td,
.table > tfoot > tr.success > td,
.table > thead > tr.success > th,
.table > tbody > tr.success > th,
.table > tfoot > tr.success > th {
  background-color: #dff0d8;
}
.table-hover > tbody > tr > td.success:hover,
.table-hover > tbody > tr > th.success:hover,
.table-hover > tbody > tr.success:hover > td,
.table-hover > tbody > tr:hover > .success,
.table-hover > tbody > tr.success:hover > th {
  background-color: #d0e9c6;
}
.table > thead > tr > td.info,
.table > tbody > tr > td.info,
.table > tfoot > tr > td.info,
.table > thead > tr > th.info,
.table > tbody > tr > th.info,
.table > tfoot > tr > th.info,
.table > thead > tr.info > td,
.table > tbody > tr.info > td,
.table > tfoot > tr.info > td,
.table > thead > tr.info > th,
.table > tbody > tr.info > th,
.table > tfoot > tr.info > th {
  background-color: #d9edf7;
}
.table-hover > tbody > tr > td.info:hover,
.table-hover > tbody > tr > th.info:hover,
.table-hover > tbody > tr.info:hover > td,
.table-hover > tbody > tr:hover > .info,
.table-hover > tbody > tr.info:hover > th {
  background-color: #c4e3f3;
}
.table > thead > tr > td.warning,
.table > tbody > tr > td.warning,
.table > tfoot > tr > td.warning,
.table > thead > tr > th.warning,
.table > tbody > tr > th.warning,
.table > tfoot > tr > th.warning,
.table > thead > tr.warning > td,
.table > tbody > tr.warning > td,
.table > tfoot > tr.warning > td,
.table > thead > tr.warning > th,
.table > tbody > tr.warning > th,
.table > tfoot > tr.warning > th {
  background-color: #fcf8e3;
}
.table-hover > tbody > tr > td.warning:hover,
.table-hover > tbody > tr > th.warning:hover,
.table-hover > tbody > tr.warning:hover > td,
.table-hover > tbody > tr:hover > .warning,
.table-hover > tbody > tr.warning:hover > th {
  background-color: #faf2cc;
}
.table > thead > tr > td.danger,
.table > tbody > tr > td.danger,
.table > tfoot > tr > td.danger,
.table > thead > tr > th.danger,
.table > tbody > tr > th.danger,
.table > tfoot > tr > th.danger,
.table > thead > tr.danger > td,
.table > tbody > tr.danger > td,
.table > tfoot > tr.danger > td,
.table > thead > tr.danger > th,
.table > tbody > tr.danger > th,
.table > tfoot > tr.danger > th {
  background-color: #f2dede;
}
.table-hover > tbody > tr > td.danger:hover,
.table-hover > tbody > tr > th.danger:hover,
.table-hover > tbody > tr.danger:hover > td,
.table-hover > tbody > tr:hover > .danger,
.table-hover > tbody > tr.danger:hover > th {
  background-color: #ebcccc;
}
.table-responsive {
  overflow-x: auto;
  min-height: 0.01%;
}
@media screen and (max-width: 767px) {
  .table-responsive {
    width: 100%;
    margin-bottom: 13.5px;
    overflow-y: hidden;
    -ms-overflow-style: -ms-autohiding-scrollbar;
    border: 1px solid #ddd;
  }
  .table-responsive > .table {
    margin-bottom: 0;
  }
  .table-responsive > .table > thead > tr > th,
  .table-responsive > .table > tbody > tr > th,
  .table-responsive > .table > tfoot > tr > th,
  .table-responsive > .table > thead > tr > td,
  .table-responsive > .table > tbody > tr > td,
  .table-responsive > .table > tfoot > tr > td {
    white-space: nowrap;
  }
  .table-responsive > .table-bordered {
    border: 0;
  }
  .table-responsive > .table-bordered > thead > tr > th:first-child,
  .table-responsive > .table-bordered > tbody > tr > th:first-child,
  .table-responsive > .table-bordered > tfoot > tr > th:first-child,
  .table-responsive > .table-bordered > thead > tr > td:first-child,
  .table-responsive > .table-bordered > tbody > tr > td:first-child,
  .table-responsive > .table-bordered > tfoot > tr > td:first-child {
    border-left: 0;
  }
  .table-responsive > .table-bordered > thead > tr > th:last-child,
  .table-responsive > .table-bordered > tbody > tr > th:last-child,
  .table-responsive > .table-bordered > tfoot > tr > th:last-child,
  .table-responsive > .table-bordered > thead > tr > td:last-child,
  .table-responsive > .table-bordered > tbody > tr > td:last-child,
  .table-responsive > .table-bordered > tfoot > tr > td:last-child {
    border-right: 0;
  }
  .table-responsive > .table-bordered > tbody > tr:last-child > th,
  .table-responsive > .table-bordered > tfoot > tr:last-child > th,
  .table-responsive > .table-bordered > tbody > tr:last-child > td,
  .table-responsive > .table-bordered > tfoot > tr:last-child > td {
    border-bottom: 0;
  }
}
fieldset {
  padding: 0;
  margin: 0;
  border: 0;
  min-width: 0;
}
legend {
  display: block;
  width: 100%;
  padding: 0;
  margin-bottom: 18px;
  font-size: 19.5px;
  line-height: inherit;
  color: #333333;
  border: 0;
  border-bottom: 1px solid #e5e5e5;
}
label {
  display: inline-block;
  max-width: 100%;
  margin-bottom: 5px;
  font-weight: bold;
}
input[type="search"] {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
input[type="radio"],
input[type="checkbox"] {
  margin: 4px 0 0;
  margin-top: 1px \9;
  line-height: normal;
}
input[type="file"] {
  display: block;
}
input[type="range"] {
  display: block;
  width: 100%;
}
select[multiple],
select[size] {
  height: auto;
}
input[type="file"]:focus,
input[type="radio"]:focus,
input[type="checkbox"]:focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
output {
  display: block;
  padding-top: 7px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
}
.form-control {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
}
.form-control:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.form-control::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.form-control:-ms-input-placeholder {
  color: #999;
}
.form-control::-webkit-input-placeholder {
  color: #999;
}
.form-control::-ms-expand {
  border: 0;
  background-color: transparent;
}
.form-control[disabled],
.form-control[readonly],
fieldset[disabled] .form-control {
  background-color: #eeeeee;
  opacity: 1;
}
.form-control[disabled],
fieldset[disabled] .form-control {
  cursor: not-allowed;
}
textarea.form-control {
  height: auto;
}
input[type="search"] {
  -webkit-appearance: none;
}
@media screen and (-webkit-min-device-pixel-ratio: 0) {
  input[type="date"].form-control,
  input[type="time"].form-control,
  input[type="datetime-local"].form-control,
  input[type="month"].form-control {
    line-height: 32px;
  }
  input[type="date"].input-sm,
  input[type="time"].input-sm,
  input[type="datetime-local"].input-sm,
  input[type="month"].input-sm,
  .input-group-sm input[type="date"],
  .input-group-sm input[type="time"],
  .input-group-sm input[type="datetime-local"],
  .input-group-sm input[type="month"] {
    line-height: 30px;
  }
  input[type="date"].input-lg,
  input[type="time"].input-lg,
  input[type="datetime-local"].input-lg,
  input[type="month"].input-lg,
  .input-group-lg input[type="date"],
  .input-group-lg input[type="time"],
  .input-group-lg input[type="datetime-local"],
  .input-group-lg input[type="month"] {
    line-height: 45px;
  }
}
.form-group {
  margin-bottom: 15px;
}
.radio,
.checkbox {
  position: relative;
  display: block;
  margin-top: 10px;
  margin-bottom: 10px;
}
.radio label,
.checkbox label {
  min-height: 18px;
  padding-left: 20px;
  margin-bottom: 0;
  font-weight: normal;
  cursor: pointer;
}
.radio input[type="radio"],
.radio-inline input[type="radio"],
.checkbox input[type="checkbox"],
.checkbox-inline input[type="checkbox"] {
  position: absolute;
  margin-left: -20px;
  margin-top: 4px \9;
}
.radio + .radio,
.checkbox + .checkbox {
  margin-top: -5px;
}
.radio-inline,
.checkbox-inline {
  position: relative;
  display: inline-block;
  padding-left: 20px;
  margin-bottom: 0;
  vertical-align: middle;
  font-weight: normal;
  cursor: pointer;
}
.radio-inline + .radio-inline,
.checkbox-inline + .checkbox-inline {
  margin-top: 0;
  margin-left: 10px;
}
input[type="radio"][disabled],
input[type="checkbox"][disabled],
input[type="radio"].disabled,
input[type="checkbox"].disabled,
fieldset[disabled] input[type="radio"],
fieldset[disabled] input[type="checkbox"] {
  cursor: not-allowed;
}
.radio-inline.disabled,
.checkbox-inline.disabled,
fieldset[disabled] .radio-inline,
fieldset[disabled] .checkbox-inline {
  cursor: not-allowed;
}
.radio.disabled label,
.checkbox.disabled label,
fieldset[disabled] .radio label,
fieldset[disabled] .checkbox label {
  cursor: not-allowed;
}
.form-control-static {
  padding-top: 7px;
  padding-bottom: 7px;
  margin-bottom: 0;
  min-height: 31px;
}
.form-control-static.input-lg,
.form-control-static.input-sm {
  padding-left: 0;
  padding-right: 0;
}
.input-sm {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
select.input-sm {
  height: 30px;
  line-height: 30px;
}
textarea.input-sm,
select[multiple].input-sm {
  height: auto;
}
.form-group-sm .form-control {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.form-group-sm select.form-control {
  height: 30px;
  line-height: 30px;
}
.form-group-sm textarea.form-control,
.form-group-sm select[multiple].form-control {
  height: auto;
}
.form-group-sm .form-control-static {
  height: 30px;
  min-height: 30px;
  padding: 6px 10px;
  font-size: 12px;
  line-height: 1.5;
}
.input-lg {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
select.input-lg {
  height: 45px;
  line-height: 45px;
}
textarea.input-lg,
select[multiple].input-lg {
  height: auto;
}
.form-group-lg .form-control {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
.form-group-lg select.form-control {
  height: 45px;
  line-height: 45px;
}
.form-group-lg textarea.form-control,
.form-group-lg select[multiple].form-control {
  height: auto;
}
.form-group-lg .form-control-static {
  height: 45px;
  min-height: 35px;
  padding: 11px 16px;
  font-size: 17px;
  line-height: 1.3333333;
}
.has-feedback {
  position: relative;
}
.has-feedback .form-control {
  padding-right: 40px;
}
.form-control-feedback {
  position: absolute;
  top: 0;
  right: 0;
  z-index: 2;
  display: block;
  width: 32px;
  height: 32px;
  line-height: 32px;
  text-align: center;
  pointer-events: none;
}
.input-lg + .form-control-feedback,
.input-group-lg + .form-control-feedback,
.form-group-lg .form-control + .form-control-feedback {
  width: 45px;
  height: 45px;
  line-height: 45px;
}
.input-sm + .form-control-feedback,
.input-group-sm + .form-control-feedback,
.form-group-sm .form-control + .form-control-feedback {
  width: 30px;
  height: 30px;
  line-height: 30px;
}
.has-success .help-block,
.has-success .control-label,
.has-success .radio,
.has-success .checkbox,
.has-success .radio-inline,
.has-success .checkbox-inline,
.has-success.radio label,
.has-success.checkbox label,
.has-success.radio-inline label,
.has-success.checkbox-inline label {
  color: #3c763d;
}
.has-success .form-control {
  border-color: #3c763d;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-success .form-control:focus {
  border-color: #2b542c;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #67b168;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #67b168;
}
.has-success .input-group-addon {
  color: #3c763d;
  border-color: #3c763d;
  background-color: #dff0d8;
}
.has-success .form-control-feedback {
  color: #3c763d;
}
.has-warning .help-block,
.has-warning .control-label,
.has-warning .radio,
.has-warning .checkbox,
.has-warning .radio-inline,
.has-warning .checkbox-inline,
.has-warning.radio label,
.has-warning.checkbox label,
.has-warning.radio-inline label,
.has-warning.checkbox-inline label {
  color: #8a6d3b;
}
.has-warning .form-control {
  border-color: #8a6d3b;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-warning .form-control:focus {
  border-color: #66512c;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #c0a16b;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #c0a16b;
}
.has-warning .input-group-addon {
  color: #8a6d3b;
  border-color: #8a6d3b;
  background-color: #fcf8e3;
}
.has-warning .form-control-feedback {
  color: #8a6d3b;
}
.has-error .help-block,
.has-error .control-label,
.has-error .radio,
.has-error .checkbox,
.has-error .radio-inline,
.has-error .checkbox-inline,
.has-error.radio label,
.has-error.checkbox label,
.has-error.radio-inline label,
.has-error.checkbox-inline label {
  color: #a94442;
}
.has-error .form-control {
  border-color: #a94442;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-error .form-control:focus {
  border-color: #843534;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #ce8483;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #ce8483;
}
.has-error .input-group-addon {
  color: #a94442;
  border-color: #a94442;
  background-color: #f2dede;
}
.has-error .form-control-feedback {
  color: #a94442;
}
.has-feedback label ~ .form-control-feedback {
  top: 23px;
}
.has-feedback label.sr-only ~ .form-control-feedback {
  top: 0;
}
.help-block {
  display: block;
  margin-top: 5px;
  margin-bottom: 10px;
  color: #404040;
}
@media (min-width: 768px) {
  .form-inline .form-group {
    display: inline-block;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .form-control {
    display: inline-block;
    width: auto;
    vertical-align: middle;
  }
  .form-inline .form-control-static {
    display: inline-block;
  }
  .form-inline .input-group {
    display: inline-table;
    vertical-align: middle;
  }
  .form-inline .input-group .input-group-addon,
  .form-inline .input-group .input-group-btn,
  .form-inline .input-group .form-control {
    width: auto;
  }
  .form-inline .input-group > .form-control {
    width: 100%;
  }
  .form-inline .control-label {
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .radio,
  .form-inline .checkbox {
    display: inline-block;
    margin-top: 0;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .radio label,
  .form-inline .checkbox label {
    padding-left: 0;
  }
  .form-inline .radio input[type="radio"],
  .form-inline .checkbox input[type="checkbox"] {
    position: relative;
    margin-left: 0;
  }
  .form-inline .has-feedback .form-control-feedback {
    top: 0;
  }
}
.form-horizontal .radio,
.form-horizontal .checkbox,
.form-horizontal .radio-inline,
.form-horizontal .checkbox-inline {
  margin-top: 0;
  margin-bottom: 0;
  padding-top: 7px;
}
.form-horizontal .radio,
.form-horizontal .checkbox {
  min-height: 25px;
}
.form-horizontal .form-group {
  margin-left: 0px;
  margin-right: 0px;
}
@media (min-width: 768px) {
  .form-horizontal .control-label {
    text-align: right;
    margin-bottom: 0;
    padding-top: 7px;
  }
}
.form-horizontal .has-feedback .form-control-feedback {
  right: 0px;
}
@media (min-width: 768px) {
  .form-horizontal .form-group-lg .control-label {
    padding-top: 11px;
    font-size: 17px;
  }
}
@media (min-width: 768px) {
  .form-horizontal .form-group-sm .control-label {
    padding-top: 6px;
    font-size: 12px;
  }
}
.btn {
  display: inline-block;
  margin-bottom: 0;
  font-weight: normal;
  text-align: center;
  vertical-align: middle;
  touch-action: manipulation;
  cursor: pointer;
  background-image: none;
  border: 1px solid transparent;
  white-space: nowrap;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  border-radius: 2px;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
.btn:focus,
.btn:active:focus,
.btn.active:focus,
.btn.focus,
.btn:active.focus,
.btn.active.focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
.btn:hover,
.btn:focus,
.btn.focus {
  color: #333;
  text-decoration: none;
}
.btn:active,
.btn.active {
  outline: 0;
  background-image: none;
  -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
  box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
}
.btn.disabled,
.btn[disabled],
fieldset[disabled] .btn {
  cursor: not-allowed;
  opacity: 0.65;
  filter: alpha(opacity=65);
  -webkit-box-shadow: none;
  box-shadow: none;
}
a.btn.disabled,
fieldset[disabled] a.btn {
  pointer-events: none;
}
.btn-default {
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
.btn-default:focus,
.btn-default.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
.btn-default:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.btn-default:active,
.btn-default.active,
.open > .dropdown-toggle.btn-default {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.btn-default:active:hover,
.btn-default.active:hover,
.open > .dropdown-toggle.btn-default:hover,
.btn-default:active:focus,
.btn-default.active:focus,
.open > .dropdown-toggle.btn-default:focus,
.btn-default:active.focus,
.btn-default.active.focus,
.open > .dropdown-toggle.btn-default.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
.btn-default:active,
.btn-default.active,
.open > .dropdown-toggle.btn-default {
  background-image: none;
}
.btn-default.disabled:hover,
.btn-default[disabled]:hover,
fieldset[disabled] .btn-default:hover,
.btn-default.disabled:focus,
.btn-default[disabled]:focus,
fieldset[disabled] .btn-default:focus,
.btn-default.disabled.focus,
.btn-default[disabled].focus,
fieldset[disabled] .btn-default.focus {
  background-color: #fff;
  border-color: #ccc;
}
.btn-default .badge {
  color: #fff;
  background-color: #333;
}
.btn-primary {
  color: #fff;
  background-color: #337ab7;
  border-color: #2e6da4;
}
.btn-primary:focus,
.btn-primary.focus {
  color: #fff;
  background-color: #286090;
  border-color: #122b40;
}
.btn-primary:hover {
  color: #fff;
  background-color: #286090;
  border-color: #204d74;
}
.btn-primary:active,
.btn-primary.active,
.open > .dropdown-toggle.btn-primary {
  color: #fff;
  background-color: #286090;
  border-color: #204d74;
}
.btn-primary:active:hover,
.btn-primary.active:hover,
.open > .dropdown-toggle.btn-primary:hover,
.btn-primary:active:focus,
.btn-primary.active:focus,
.open > .dropdown-toggle.btn-primary:focus,
.btn-primary:active.focus,
.btn-primary.active.focus,
.open > .dropdown-toggle.btn-primary.focus {
  color: #fff;
  background-color: #204d74;
  border-color: #122b40;
}
.btn-primary:active,
.btn-primary.active,
.open > .dropdown-toggle.btn-primary {
  background-image: none;
}
.btn-primary.disabled:hover,
.btn-primary[disabled]:hover,
fieldset[disabled] .btn-primary:hover,
.btn-primary.disabled:focus,
.btn-primary[disabled]:focus,
fieldset[disabled] .btn-primary:focus,
.btn-primary.disabled.focus,
.btn-primary[disabled].focus,
fieldset[disabled] .btn-primary.focus {
  background-color: #337ab7;
  border-color: #2e6da4;
}
.btn-primary .badge {
  color: #337ab7;
  background-color: #fff;
}
.btn-success {
  color: #fff;
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.btn-success:focus,
.btn-success.focus {
  color: #fff;
  background-color: #449d44;
  border-color: #255625;
}
.btn-success:hover {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.btn-success:active,
.btn-success.active,
.open > .dropdown-toggle.btn-success {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.btn-success:active:hover,
.btn-success.active:hover,
.open > .dropdown-toggle.btn-success:hover,
.btn-success:active:focus,
.btn-success.active:focus,
.open > .dropdown-toggle.btn-success:focus,
.btn-success:active.focus,
.btn-success.active.focus,
.open > .dropdown-toggle.btn-success.focus {
  color: #fff;
  background-color: #398439;
  border-color: #255625;
}
.btn-success:active,
.btn-success.active,
.open > .dropdown-toggle.btn-success {
  background-image: none;
}
.btn-success.disabled:hover,
.btn-success[disabled]:hover,
fieldset[disabled] .btn-success:hover,
.btn-success.disabled:focus,
.btn-success[disabled]:focus,
fieldset[disabled] .btn-success:focus,
.btn-success.disabled.focus,
.btn-success[disabled].focus,
fieldset[disabled] .btn-success.focus {
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.btn-success .badge {
  color: #5cb85c;
  background-color: #fff;
}
.btn-info {
  color: #fff;
  background-color: #5bc0de;
  border-color: #46b8da;
}
.btn-info:focus,
.btn-info.focus {
  color: #fff;
  background-color: #31b0d5;
  border-color: #1b6d85;
}
.btn-info:hover {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.btn-info:active,
.btn-info.active,
.open > .dropdown-toggle.btn-info {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.btn-info:active:hover,
.btn-info.active:hover,
.open > .dropdown-toggle.btn-info:hover,
.btn-info:active:focus,
.btn-info.active:focus,
.open > .dropdown-toggle.btn-info:focus,
.btn-info:active.focus,
.btn-info.active.focus,
.open > .dropdown-toggle.btn-info.focus {
  color: #fff;
  background-color: #269abc;
  border-color: #1b6d85;
}
.btn-info:active,
.btn-info.active,
.open > .dropdown-toggle.btn-info {
  background-image: none;
}
.btn-info.disabled:hover,
.btn-info[disabled]:hover,
fieldset[disabled] .btn-info:hover,
.btn-info.disabled:focus,
.btn-info[disabled]:focus,
fieldset[disabled] .btn-info:focus,
.btn-info.disabled.focus,
.btn-info[disabled].focus,
fieldset[disabled] .btn-info.focus {
  background-color: #5bc0de;
  border-color: #46b8da;
}
.btn-info .badge {
  color: #5bc0de;
  background-color: #fff;
}
.btn-warning {
  color: #fff;
  background-color: #f0ad4e;
  border-color: #eea236;
}
.btn-warning:focus,
.btn-warning.focus {
  color: #fff;
  background-color: #ec971f;
  border-color: #985f0d;
}
.btn-warning:hover {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.btn-warning:active,
.btn-warning.active,
.open > .dropdown-toggle.btn-warning {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.btn-warning:active:hover,
.btn-warning.active:hover,
.open > .dropdown-toggle.btn-warning:hover,
.btn-warning:active:focus,
.btn-warning.active:focus,
.open > .dropdown-toggle.btn-warning:focus,
.btn-warning:active.focus,
.btn-warning.active.focus,
.open > .dropdown-toggle.btn-warning.focus {
  color: #fff;
  background-color: #d58512;
  border-color: #985f0d;
}
.btn-warning:active,
.btn-warning.active,
.open > .dropdown-toggle.btn-warning {
  background-image: none;
}
.btn-warning.disabled:hover,
.btn-warning[disabled]:hover,
fieldset[disabled] .btn-warning:hover,
.btn-warning.disabled:focus,
.btn-warning[disabled]:focus,
fieldset[disabled] .btn-warning:focus,
.btn-warning.disabled.focus,
.btn-warning[disabled].focus,
fieldset[disabled] .btn-warning.focus {
  background-color: #f0ad4e;
  border-color: #eea236;
}
.btn-warning .badge {
  color: #f0ad4e;
  background-color: #fff;
}
.btn-danger {
  color: #fff;
  background-color: #d9534f;
  border-color: #d43f3a;
}
.btn-danger:focus,
.btn-danger.focus {
  color: #fff;
  background-color: #c9302c;
  border-color: #761c19;
}
.btn-danger:hover {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.btn-danger:active,
.btn-danger.active,
.open > .dropdown-toggle.btn-danger {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.btn-danger:active:hover,
.btn-danger.active:hover,
.open > .dropdown-toggle.btn-danger:hover,
.btn-danger:active:focus,
.btn-danger.active:focus,
.open > .dropdown-toggle.btn-danger:focus,
.btn-danger:active.focus,
.btn-danger.active.focus,
.open > .dropdown-toggle.btn-danger.focus {
  color: #fff;
  background-color: #ac2925;
  border-color: #761c19;
}
.btn-danger:active,
.btn-danger.active,
.open > .dropdown-toggle.btn-danger {
  background-image: none;
}
.btn-danger.disabled:hover,
.btn-danger[disabled]:hover,
fieldset[disabled] .btn-danger:hover,
.btn-danger.disabled:focus,
.btn-danger[disabled]:focus,
fieldset[disabled] .btn-danger:focus,
.btn-danger.disabled.focus,
.btn-danger[disabled].focus,
fieldset[disabled] .btn-danger.focus {
  background-color: #d9534f;
  border-color: #d43f3a;
}
.btn-danger .badge {
  color: #d9534f;
  background-color: #fff;
}
.btn-link {
  color: #337ab7;
  font-weight: normal;
  border-radius: 0;
}
.btn-link,
.btn-link:active,
.btn-link.active,
.btn-link[disabled],
fieldset[disabled] .btn-link {
  background-color: transparent;
  -webkit-box-shadow: none;
  box-shadow: none;
}
.btn-link,
.btn-link:hover,
.btn-link:focus,
.btn-link:active {
  border-color: transparent;
}
.btn-link:hover,
.btn-link:focus {
  color: #23527c;
  text-decoration: underline;
  background-color: transparent;
}
.btn-link[disabled]:hover,
fieldset[disabled] .btn-link:hover,
.btn-link[disabled]:focus,
fieldset[disabled] .btn-link:focus {
  color: #777777;
  text-decoration: none;
}
.btn-lg,
.btn-group-lg > .btn {
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
.btn-sm,
.btn-group-sm > .btn {
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.btn-xs,
.btn-group-xs > .btn {
  padding: 1px 5px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.btn-block {
  display: block;
  width: 100%;
}
.btn-block + .btn-block {
  margin-top: 5px;
}
input[type="submit"].btn-block,
input[type="reset"].btn-block,
input[type="button"].btn-block {
  width: 100%;
}
.fade {
  opacity: 0;
  -webkit-transition: opacity 0.15s linear;
  -o-transition: opacity 0.15s linear;
  transition: opacity 0.15s linear;
}
.fade.in {
  opacity: 1;
}
.collapse {
  display: none;
}
.collapse.in {
  display: block;
}
tr.collapse.in {
  display: table-row;
}
tbody.collapse.in {
  display: table-row-group;
}
.collapsing {
  position: relative;
  height: 0;
  overflow: hidden;
  -webkit-transition-property: height, visibility;
  transition-property: height, visibility;
  -webkit-transition-duration: 0.35s;
  transition-duration: 0.35s;
  -webkit-transition-timing-function: ease;
  transition-timing-function: ease;
}
.caret {
  display: inline-block;
  width: 0;
  height: 0;
  margin-left: 2px;
  vertical-align: middle;
  border-top: 4px dashed;
  border-top: 4px solid \9;
  border-right: 4px solid transparent;
  border-left: 4px solid transparent;
}
.dropup,
.dropdown {
  position: relative;
}
.dropdown-toggle:focus {
  outline: 0;
}
.dropdown-menu {
  position: absolute;
  top: 100%;
  left: 0;
  z-index: 1000;
  display: none;
  float: left;
  min-width: 160px;
  padding: 5px 0;
  margin: 2px 0 0;
  list-style: none;
  font-size: 13px;
  text-align: left;
  background-color: #fff;
  border: 1px solid #ccc;
  border: 1px solid rgba(0, 0, 0, 0.15);
  border-radius: 2px;
  -webkit-box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);
  background-clip: padding-box;
}
.dropdown-menu.pull-right {
  right: 0;
  left: auto;
}
.dropdown-menu .divider {
  height: 1px;
  margin: 8px 0;
  overflow: hidden;
  background-color: #e5e5e5;
}
.dropdown-menu > li > a {
  display: block;
  padding: 3px 20px;
  clear: both;
  font-weight: normal;
  line-height: 1.42857143;
  color: #333333;
  white-space: nowrap;
}
.dropdown-menu > li > a:hover,
.dropdown-menu > li > a:focus {
  text-decoration: none;
  color: #262626;
  background-color: #f5f5f5;
}
.dropdown-menu > .active > a,
.dropdown-menu > .active > a:hover,
.dropdown-menu > .active > a:focus {
  color: #fff;
  text-decoration: none;
  outline: 0;
  background-color: #337ab7;
}
.dropdown-menu > .disabled > a,
.dropdown-menu > .disabled > a:hover,
.dropdown-menu > .disabled > a:focus {
  color: #777777;
}
.dropdown-menu > .disabled > a:hover,
.dropdown-menu > .disabled > a:focus {
  text-decoration: none;
  background-color: transparent;
  background-image: none;
  filter: progid:DXImageTransform.Microsoft.gradient(enabled = false);
  cursor: not-allowed;
}
.open > .dropdown-menu {
  display: block;
}
.open > a {
  outline: 0;
}
.dropdown-menu-right {
  left: auto;
  right: 0;
}
.dropdown-menu-left {
  left: 0;
  right: auto;
}
.dropdown-header {
  display: block;
  padding: 3px 20px;
  font-size: 12px;
  line-height: 1.42857143;
  color: #777777;
  white-space: nowrap;
}
.dropdown-backdrop {
  position: fixed;
  left: 0;
  right: 0;
  bottom: 0;
  top: 0;
  z-index: 990;
}
.pull-right > .dropdown-menu {
  right: 0;
  left: auto;
}
.dropup .caret,
.navbar-fixed-bottom .dropdown .caret {
  border-top: 0;
  border-bottom: 4px dashed;
  border-bottom: 4px solid \9;
  content: "";
}
.dropup .dropdown-menu,
.navbar-fixed-bottom .dropdown .dropdown-menu {
  top: auto;
  bottom: 100%;
  margin-bottom: 2px;
}
@media (min-width: 541px) {
  .navbar-right .dropdown-menu {
    left: auto;
    right: 0;
  }
  .navbar-right .dropdown-menu-left {
    left: 0;
    right: auto;
  }
}
.btn-group,
.btn-group-vertical {
  position: relative;
  display: inline-block;
  vertical-align: middle;
}
.btn-group > .btn,
.btn-group-vertical > .btn {
  position: relative;
  float: left;
}
.btn-group > .btn:hover,
.btn-group-vertical > .btn:hover,
.btn-group > .btn:focus,
.btn-group-vertical > .btn:focus,
.btn-group > .btn:active,
.btn-group-vertical > .btn:active,
.btn-group > .btn.active,
.btn-group-vertical > .btn.active {
  z-index: 2;
}
.btn-group .btn + .btn,
.btn-group .btn + .btn-group,
.btn-group .btn-group + .btn,
.btn-group .btn-group + .btn-group {
  margin-left: -1px;
}
.btn-toolbar {
  margin-left: -5px;
}
.btn-toolbar .btn,
.btn-toolbar .btn-group,
.btn-toolbar .input-group {
  float: left;
}
.btn-toolbar > .btn,
.btn-toolbar > .btn-group,
.btn-toolbar > .input-group {
  margin-left: 5px;
}
.btn-group > .btn:not(:first-child):not(:last-child):not(.dropdown-toggle) {
  border-radius: 0;
}
.btn-group > .btn:first-child {
  margin-left: 0;
}
.btn-group > .btn:first-child:not(:last-child):not(.dropdown-toggle) {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.btn-group > .btn:last-child:not(:first-child),
.btn-group > .dropdown-toggle:not(:first-child) {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.btn-group > .btn-group {
  float: left;
}
.btn-group > .btn-group:not(:first-child):not(:last-child) > .btn {
  border-radius: 0;
}
.btn-group > .btn-group:first-child:not(:last-child) > .btn:last-child,
.btn-group > .btn-group:first-child:not(:last-child) > .dropdown-toggle {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.btn-group > .btn-group:last-child:not(:first-child) > .btn:first-child {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.btn-group .dropdown-toggle:active,
.btn-group.open .dropdown-toggle {
  outline: 0;
}
.btn-group > .btn + .dropdown-toggle {
  padding-left: 8px;
  padding-right: 8px;
}
.btn-group > .btn-lg + .dropdown-toggle {
  padding-left: 12px;
  padding-right: 12px;
}
.btn-group.open .dropdown-toggle {
  -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
  box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
}
.btn-group.open .dropdown-toggle.btn-link {
  -webkit-box-shadow: none;
  box-shadow: none;
}
.btn .caret {
  margin-left: 0;
}
.btn-lg .caret {
  border-width: 5px 5px 0;
  border-bottom-width: 0;
}
.dropup .btn-lg .caret {
  border-width: 0 5px 5px;
}
.btn-group-vertical > .btn,
.btn-group-vertical > .btn-group,
.btn-group-vertical > .btn-group > .btn {
  display: block;
  float: none;
  width: 100%;
  max-width: 100%;
}
.btn-group-vertical > .btn-group > .btn {
  float: none;
}
.btn-group-vertical > .btn + .btn,
.btn-group-vertical > .btn + .btn-group,
.btn-group-vertical > .btn-group + .btn,
.btn-group-vertical > .btn-group + .btn-group {
  margin-top: -1px;
  margin-left: 0;
}
.btn-group-vertical > .btn:not(:first-child):not(:last-child) {
  border-radius: 0;
}
.btn-group-vertical > .btn:first-child:not(:last-child) {
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.btn-group-vertical > .btn:last-child:not(:first-child) {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
  border-bottom-right-radius: 2px;
  border-bottom-left-radius: 2px;
}
.btn-group-vertical > .btn-group:not(:first-child):not(:last-child) > .btn {
  border-radius: 0;
}
.btn-group-vertical > .btn-group:first-child:not(:last-child) > .btn:last-child,
.btn-group-vertical > .btn-group:first-child:not(:last-child) > .dropdown-toggle {
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.btn-group-vertical > .btn-group:last-child:not(:first-child) > .btn:first-child {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.btn-group-justified {
  display: table;
  width: 100%;
  table-layout: fixed;
  border-collapse: separate;
}
.btn-group-justified > .btn,
.btn-group-justified > .btn-group {
  float: none;
  display: table-cell;
  width: 1%;
}
.btn-group-justified > .btn-group .btn {
  width: 100%;
}
.btn-group-justified > .btn-group .dropdown-menu {
  left: auto;
}
[data-toggle="buttons"] > .btn input[type="radio"],
[data-toggle="buttons"] > .btn-group > .btn input[type="radio"],
[data-toggle="buttons"] > .btn input[type="checkbox"],
[data-toggle="buttons"] > .btn-group > .btn input[type="checkbox"] {
  position: absolute;
  clip: rect(0, 0, 0, 0);
  pointer-events: none;
}
.input-group {
  position: relative;
  display: table;
  border-collapse: separate;
}
.input-group[class*="col-"] {
  float: none;
  padding-left: 0;
  padding-right: 0;
}
.input-group .form-control {
  position: relative;
  z-index: 2;
  float: left;
  width: 100%;
  margin-bottom: 0;
}
.input-group .form-control:focus {
  z-index: 3;
}
.input-group-lg > .form-control,
.input-group-lg > .input-group-addon,
.input-group-lg > .input-group-btn > .btn {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
select.input-group-lg > .form-control,
select.input-group-lg > .input-group-addon,
select.input-group-lg > .input-group-btn > .btn {
  height: 45px;
  line-height: 45px;
}
textarea.input-group-lg > .form-control,
textarea.input-group-lg > .input-group-addon,
textarea.input-group-lg > .input-group-btn > .btn,
select[multiple].input-group-lg > .form-control,
select[multiple].input-group-lg > .input-group-addon,
select[multiple].input-group-lg > .input-group-btn > .btn {
  height: auto;
}
.input-group-sm > .form-control,
.input-group-sm > .input-group-addon,
.input-group-sm > .input-group-btn > .btn {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
select.input-group-sm > .form-control,
select.input-group-sm > .input-group-addon,
select.input-group-sm > .input-group-btn > .btn {
  height: 30px;
  line-height: 30px;
}
textarea.input-group-sm > .form-control,
textarea.input-group-sm > .input-group-addon,
textarea.input-group-sm > .input-group-btn > .btn,
select[multiple].input-group-sm > .form-control,
select[multiple].input-group-sm > .input-group-addon,
select[multiple].input-group-sm > .input-group-btn > .btn {
  height: auto;
}
.input-group-addon,
.input-group-btn,
.input-group .form-control {
  display: table-cell;
}
.input-group-addon:not(:first-child):not(:last-child),
.input-group-btn:not(:first-child):not(:last-child),
.input-group .form-control:not(:first-child):not(:last-child) {
  border-radius: 0;
}
.input-group-addon,
.input-group-btn {
  width: 1%;
  white-space: nowrap;
  vertical-align: middle;
}
.input-group-addon {
  padding: 6px 12px;
  font-size: 13px;
  font-weight: normal;
  line-height: 1;
  color: #555555;
  text-align: center;
  background-color: #eeeeee;
  border: 1px solid #ccc;
  border-radius: 2px;
}
.input-group-addon.input-sm {
  padding: 5px 10px;
  font-size: 12px;
  border-radius: 1px;
}
.input-group-addon.input-lg {
  padding: 10px 16px;
  font-size: 17px;
  border-radius: 3px;
}
.input-group-addon input[type="radio"],
.input-group-addon input[type="checkbox"] {
  margin-top: 0;
}
.input-group .form-control:first-child,
.input-group-addon:first-child,
.input-group-btn:first-child > .btn,
.input-group-btn:first-child > .btn-group > .btn,
.input-group-btn:first-child > .dropdown-toggle,
.input-group-btn:last-child > .btn:not(:last-child):not(.dropdown-toggle),
.input-group-btn:last-child > .btn-group:not(:last-child) > .btn {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.input-group-addon:first-child {
  border-right: 0;
}
.input-group .form-control:last-child,
.input-group-addon:last-child,
.input-group-btn:last-child > .btn,
.input-group-btn:last-child > .btn-group > .btn,
.input-group-btn:last-child > .dropdown-toggle,
.input-group-btn:first-child > .btn:not(:first-child),
.input-group-btn:first-child > .btn-group:not(:first-child) > .btn {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.input-group-addon:last-child {
  border-left: 0;
}
.input-group-btn {
  position: relative;
  font-size: 0;
  white-space: nowrap;
}
.input-group-btn > .btn {
  position: relative;
}
.input-group-btn > .btn + .btn {
  margin-left: -1px;
}
.input-group-btn > .btn:hover,
.input-group-btn > .btn:focus,
.input-group-btn > .btn:active {
  z-index: 2;
}
.input-group-btn:first-child > .btn,
.input-group-btn:first-child > .btn-group {
  margin-right: -1px;
}
.input-group-btn:last-child > .btn,
.input-group-btn:last-child > .btn-group {
  z-index: 2;
  margin-left: -1px;
}
.nav {
  margin-bottom: 0;
  padding-left: 0;
  list-style: none;
}
.nav > li {
  position: relative;
  display: block;
}
.nav > li > a {
  position: relative;
  display: block;
  padding: 10px 15px;
}
.nav > li > a:hover,
.nav > li > a:focus {
  text-decoration: none;
  background-color: #eeeeee;
}
.nav > li.disabled > a {
  color: #777777;
}
.nav > li.disabled > a:hover,
.nav > li.disabled > a:focus {
  color: #777777;
  text-decoration: none;
  background-color: transparent;
  cursor: not-allowed;
}
.nav .open > a,
.nav .open > a:hover,
.nav .open > a:focus {
  background-color: #eeeeee;
  border-color: #337ab7;
}
.nav .nav-divider {
  height: 1px;
  margin: 8px 0;
  overflow: hidden;
  background-color: #e5e5e5;
}
.nav > li > a > img {
  max-width: none;
}
.nav-tabs {
  border-bottom: 1px solid #ddd;
}
.nav-tabs > li {
  float: left;
  margin-bottom: -1px;
}
.nav-tabs > li > a {
  margin-right: 2px;
  line-height: 1.42857143;
  border: 1px solid transparent;
  border-radius: 2px 2px 0 0;
}
.nav-tabs > li > a:hover {
  border-color: #eeeeee #eeeeee #ddd;
}
.nav-tabs > li.active > a,
.nav-tabs > li.active > a:hover,
.nav-tabs > li.active > a:focus {
  color: #555555;
  background-color: #fff;
  border: 1px solid #ddd;
  border-bottom-color: transparent;
  cursor: default;
}
.nav-tabs.nav-justified {
  width: 100%;
  border-bottom: 0;
}
.nav-tabs.nav-justified > li {
  float: none;
}
.nav-tabs.nav-justified > li > a {
  text-align: center;
  margin-bottom: 5px;
}
.nav-tabs.nav-justified > .dropdown .dropdown-menu {
  top: auto;
  left: auto;
}
@media (min-width: 768px) {
  .nav-tabs.nav-justified > li {
    display: table-cell;
    width: 1%;
  }
  .nav-tabs.nav-justified > li > a {
    margin-bottom: 0;
  }
}
.nav-tabs.nav-justified > li > a {
  margin-right: 0;
  border-radius: 2px;
}
.nav-tabs.nav-justified > .active > a,
.nav-tabs.nav-justified > .active > a:hover,
.nav-tabs.nav-justified > .active > a:focus {
  border: 1px solid #ddd;
}
@media (min-width: 768px) {
  .nav-tabs.nav-justified > li > a {
    border-bottom: 1px solid #ddd;
    border-radius: 2px 2px 0 0;
  }
  .nav-tabs.nav-justified > .active > a,
  .nav-tabs.nav-justified > .active > a:hover,
  .nav-tabs.nav-justified > .active > a:focus {
    border-bottom-color: #fff;
  }
}
.nav-pills > li {
  float: left;
}
.nav-pills > li > a {
  border-radius: 2px;
}
.nav-pills > li + li {
  margin-left: 2px;
}
.nav-pills > li.active > a,
.nav-pills > li.active > a:hover,
.nav-pills > li.active > a:focus {
  color: #fff;
  background-color: #337ab7;
}
.nav-stacked > li {
  float: none;
}
.nav-stacked > li + li {
  margin-top: 2px;
  margin-left: 0;
}
.nav-justified {
  width: 100%;
}
.nav-justified > li {
  float: none;
}
.nav-justified > li > a {
  text-align: center;
  margin-bottom: 5px;
}
.nav-justified > .dropdown .dropdown-menu {
  top: auto;
  left: auto;
}
@media (min-width: 768px) {
  .nav-justified > li {
    display: table-cell;
    width: 1%;
  }
  .nav-justified > li > a {
    margin-bottom: 0;
  }
}
.nav-tabs-justified {
  border-bottom: 0;
}
.nav-tabs-justified > li > a {
  margin-right: 0;
  border-radius: 2px;
}
.nav-tabs-justified > .active > a,
.nav-tabs-justified > .active > a:hover,
.nav-tabs-justified > .active > a:focus {
  border: 1px solid #ddd;
}
@media (min-width: 768px) {
  .nav-tabs-justified > li > a {
    border-bottom: 1px solid #ddd;
    border-radius: 2px 2px 0 0;
  }
  .nav-tabs-justified > .active > a,
  .nav-tabs-justified > .active > a:hover,
  .nav-tabs-justified > .active > a:focus {
    border-bottom-color: #fff;
  }
}
.tab-content > .tab-pane {
  display: none;
}
.tab-content > .active {
  display: block;
}
.nav-tabs .dropdown-menu {
  margin-top: -1px;
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.navbar {
  position: relative;
  min-height: 30px;
  margin-bottom: 18px;
  border: 1px solid transparent;
}
@media (min-width: 541px) {
  .navbar {
    border-radius: 2px;
  }
}
@media (min-width: 541px) {
  .navbar-header {
    float: left;
  }
}
.navbar-collapse {
  overflow-x: visible;
  padding-right: 0px;
  padding-left: 0px;
  border-top: 1px solid transparent;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1);
  -webkit-overflow-scrolling: touch;
}
.navbar-collapse.in {
  overflow-y: auto;
}
@media (min-width: 541px) {
  .navbar-collapse {
    width: auto;
    border-top: 0;
    box-shadow: none;
  }
  .navbar-collapse.collapse {
    display: block !important;
    height: auto !important;
    padding-bottom: 0;
    overflow: visible !important;
  }
  .navbar-collapse.in {
    overflow-y: visible;
  }
  .navbar-fixed-top .navbar-collapse,
  .navbar-static-top .navbar-collapse,
  .navbar-fixed-bottom .navbar-collapse {
    padding-left: 0;
    padding-right: 0;
  }
}
.navbar-fixed-top .navbar-collapse,
.navbar-fixed-bottom .navbar-collapse {
  max-height: 340px;
}
@media (max-device-width: 540px) and (orientation: landscape) {
  .navbar-fixed-top .navbar-collapse,
  .navbar-fixed-bottom .navbar-collapse {
    max-height: 200px;
  }
}
.container > .navbar-header,
.container-fluid > .navbar-header,
.container > .navbar-collapse,
.container-fluid > .navbar-collapse {
  margin-right: 0px;
  margin-left: 0px;
}
@media (min-width: 541px) {
  .container > .navbar-header,
  .container-fluid > .navbar-header,
  .container > .navbar-collapse,
  .container-fluid > .navbar-collapse {
    margin-right: 0;
    margin-left: 0;
  }
}
.navbar-static-top {
  z-index: 1000;
  border-width: 0 0 1px;
}
@media (min-width: 541px) {
  .navbar-static-top {
    border-radius: 0;
  }
}
.navbar-fixed-top,
.navbar-fixed-bottom {
  position: fixed;
  right: 0;
  left: 0;
  z-index: 1030;
}
@media (min-width: 541px) {
  .navbar-fixed-top,
  .navbar-fixed-bottom {
    border-radius: 0;
  }
}
.navbar-fixed-top {
  top: 0;
  border-width: 0 0 1px;
}
.navbar-fixed-bottom {
  bottom: 0;
  margin-bottom: 0;
  border-width: 1px 0 0;
}
.navbar-brand {
  float: left;
  padding: 6px 0px;
  font-size: 17px;
  line-height: 18px;
  height: 30px;
}
.navbar-brand:hover,
.navbar-brand:focus {
  text-decoration: none;
}
.navbar-brand > img {
  display: block;
}
@media (min-width: 541px) {
  .navbar > .container .navbar-brand,
  .navbar > .container-fluid .navbar-brand {
    margin-left: 0px;
  }
}
.navbar-toggle {
  position: relative;
  float: right;
  margin-right: 0px;
  padding: 9px 10px;
  margin-top: -2px;
  margin-bottom: -2px;
  background-color: transparent;
  background-image: none;
  border: 1px solid transparent;
  border-radius: 2px;
}
.navbar-toggle:focus {
  outline: 0;
}
.navbar-toggle .icon-bar {
  display: block;
  width: 22px;
  height: 2px;
  border-radius: 1px;
}
.navbar-toggle .icon-bar + .icon-bar {
  margin-top: 4px;
}
@media (min-width: 541px) {
  .navbar-toggle {
    display: none;
  }
}
.navbar-nav {
  margin: 3px 0px;
}
.navbar-nav > li > a {
  padding-top: 10px;
  padding-bottom: 10px;
  line-height: 18px;
}
@media (max-width: 540px) {
  .navbar-nav .open .dropdown-menu {
    position: static;
    float: none;
    width: auto;
    margin-top: 0;
    background-color: transparent;
    border: 0;
    box-shadow: none;
  }
  .navbar-nav .open .dropdown-menu > li > a,
  .navbar-nav .open .dropdown-menu .dropdown-header {
    padding: 5px 15px 5px 25px;
  }
  .navbar-nav .open .dropdown-menu > li > a {
    line-height: 18px;
  }
  .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-nav .open .dropdown-menu > li > a:focus {
    background-image: none;
  }
}
@media (min-width: 541px) {
  .navbar-nav {
    float: left;
    margin: 0;
  }
  .navbar-nav > li {
    float: left;
  }
  .navbar-nav > li > a {
    padding-top: 6px;
    padding-bottom: 6px;
  }
}
.navbar-form {
  margin-left: 0px;
  margin-right: 0px;
  padding: 10px 0px;
  border-top: 1px solid transparent;
  border-bottom: 1px solid transparent;
  -webkit-box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1), 0 1px 0 rgba(255, 255, 255, 0.1);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1), 0 1px 0 rgba(255, 255, 255, 0.1);
  margin-top: -1px;
  margin-bottom: -1px;
}
@media (min-width: 768px) {
  .navbar-form .form-group {
    display: inline-block;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .form-control {
    display: inline-block;
    width: auto;
    vertical-align: middle;
  }
  .navbar-form .form-control-static {
    display: inline-block;
  }
  .navbar-form .input-group {
    display: inline-table;
    vertical-align: middle;
  }
  .navbar-form .input-group .input-group-addon,
  .navbar-form .input-group .input-group-btn,
  .navbar-form .input-group .form-control {
    width: auto;
  }
  .navbar-form .input-group > .form-control {
    width: 100%;
  }
  .navbar-form .control-label {
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .radio,
  .navbar-form .checkbox {
    display: inline-block;
    margin-top: 0;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .radio label,
  .navbar-form .checkbox label {
    padding-left: 0;
  }
  .navbar-form .radio input[type="radio"],
  .navbar-form .checkbox input[type="checkbox"] {
    position: relative;
    margin-left: 0;
  }
  .navbar-form .has-feedback .form-control-feedback {
    top: 0;
  }
}
@media (max-width: 540px) {
  .navbar-form .form-group {
    margin-bottom: 5px;
  }
  .navbar-form .form-group:last-child {
    margin-bottom: 0;
  }
}
@media (min-width: 541px) {
  .navbar-form {
    width: auto;
    border: 0;
    margin-left: 0;
    margin-right: 0;
    padding-top: 0;
    padding-bottom: 0;
    -webkit-box-shadow: none;
    box-shadow: none;
  }
}
.navbar-nav > li > .dropdown-menu {
  margin-top: 0;
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.navbar-fixed-bottom .navbar-nav > li > .dropdown-menu {
  margin-bottom: 0;
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.navbar-btn {
  margin-top: -1px;
  margin-bottom: -1px;
}
.navbar-btn.btn-sm {
  margin-top: 0px;
  margin-bottom: 0px;
}
.navbar-btn.btn-xs {
  margin-top: 4px;
  margin-bottom: 4px;
}
.navbar-text {
  margin-top: 6px;
  margin-bottom: 6px;
}
@media (min-width: 541px) {
  .navbar-text {
    float: left;
    margin-left: 0px;
    margin-right: 0px;
  }
}
@media (min-width: 541px) {
  .navbar-left {
    float: left !important;
    float: left;
  }
  .navbar-right {
    float: right !important;
    float: right;
    margin-right: 0px;
  }
  .navbar-right ~ .navbar-right {
    margin-right: 0;
  }
}
.navbar-default {
  background-color: #f8f8f8;
  border-color: #e7e7e7;
}
.navbar-default .navbar-brand {
  color: #777;
}
.navbar-default .navbar-brand:hover,
.navbar-default .navbar-brand:focus {
  color: #5e5e5e;
  background-color: transparent;
}
.navbar-default .navbar-text {
  color: #777;
}
.navbar-default .navbar-nav > li > a {
  color: #777;
}
.navbar-default .navbar-nav > li > a:hover,
.navbar-default .navbar-nav > li > a:focus {
  color: #333;
  background-color: transparent;
}
.navbar-default .navbar-nav > .active > a,
.navbar-default .navbar-nav > .active > a:hover,
.navbar-default .navbar-nav > .active > a:focus {
  color: #555;
  background-color: #e7e7e7;
}
.navbar-default .navbar-nav > .disabled > a,
.navbar-default .navbar-nav > .disabled > a:hover,
.navbar-default .navbar-nav > .disabled > a:focus {
  color: #ccc;
  background-color: transparent;
}
.navbar-default .navbar-toggle {
  border-color: #ddd;
}
.navbar-default .navbar-toggle:hover,
.navbar-default .navbar-toggle:focus {
  background-color: #ddd;
}
.navbar-default .navbar-toggle .icon-bar {
  background-color: #888;
}
.navbar-default .navbar-collapse,
.navbar-default .navbar-form {
  border-color: #e7e7e7;
}
.navbar-default .navbar-nav > .open > a,
.navbar-default .navbar-nav > .open > a:hover,
.navbar-default .navbar-nav > .open > a:focus {
  background-color: #e7e7e7;
  color: #555;
}
@media (max-width: 540px) {
  .navbar-default .navbar-nav .open .dropdown-menu > li > a {
    color: #777;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > li > a:focus {
    color: #333;
    background-color: transparent;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a,
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a:focus {
    color: #555;
    background-color: #e7e7e7;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a,
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a:focus {
    color: #ccc;
    background-color: transparent;
  }
}
.navbar-default .navbar-link {
  color: #777;
}
.navbar-default .navbar-link:hover {
  color: #333;
}
.navbar-default .btn-link {
  color: #777;
}
.navbar-default .btn-link:hover,
.navbar-default .btn-link:focus {
  color: #333;
}
.navbar-default .btn-link[disabled]:hover,
fieldset[disabled] .navbar-default .btn-link:hover,
.navbar-default .btn-link[disabled]:focus,
fieldset[disabled] .navbar-default .btn-link:focus {
  color: #ccc;
}
.navbar-inverse {
  background-color: #222;
  border-color: #080808;
}
.navbar-inverse .navbar-brand {
  color: #9d9d9d;
}
.navbar-inverse .navbar-brand:hover,
.navbar-inverse .navbar-brand:focus {
  color: #fff;
  background-color: transparent;
}
.navbar-inverse .navbar-text {
  color: #9d9d9d;
}
.navbar-inverse .navbar-nav > li > a {
  color: #9d9d9d;
}
.navbar-inverse .navbar-nav > li > a:hover,
.navbar-inverse .navbar-nav > li > a:focus {
  color: #fff;
  background-color: transparent;
}
.navbar-inverse .navbar-nav > .active > a,
.navbar-inverse .navbar-nav > .active > a:hover,
.navbar-inverse .navbar-nav > .active > a:focus {
  color: #fff;
  background-color: #080808;
}
.navbar-inverse .navbar-nav > .disabled > a,
.navbar-inverse .navbar-nav > .disabled > a:hover,
.navbar-inverse .navbar-nav > .disabled > a:focus {
  color: #444;
  background-color: transparent;
}
.navbar-inverse .navbar-toggle {
  border-color: #333;
}
.navbar-inverse .navbar-toggle:hover,
.navbar-inverse .navbar-toggle:focus {
  background-color: #333;
}
.navbar-inverse .navbar-toggle .icon-bar {
  background-color: #fff;
}
.navbar-inverse .navbar-collapse,
.navbar-inverse .navbar-form {
  border-color: #101010;
}
.navbar-inverse .navbar-nav > .open > a,
.navbar-inverse .navbar-nav > .open > a:hover,
.navbar-inverse .navbar-nav > .open > a:focus {
  background-color: #080808;
  color: #fff;
}
@media (max-width: 540px) {
  .navbar-inverse .navbar-nav .open .dropdown-menu > .dropdown-header {
    border-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu .divider {
    background-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a {
    color: #9d9d9d;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a:focus {
    color: #fff;
    background-color: transparent;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a:focus {
    color: #fff;
    background-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a:focus {
    color: #444;
    background-color: transparent;
  }
}
.navbar-inverse .navbar-link {
  color: #9d9d9d;
}
.navbar-inverse .navbar-link:hover {
  color: #fff;
}
.navbar-inverse .btn-link {
  color: #9d9d9d;
}
.navbar-inverse .btn-link:hover,
.navbar-inverse .btn-link:focus {
  color: #fff;
}
.navbar-inverse .btn-link[disabled]:hover,
fieldset[disabled] .navbar-inverse .btn-link:hover,
.navbar-inverse .btn-link[disabled]:focus,
fieldset[disabled] .navbar-inverse .btn-link:focus {
  color: #444;
}
.breadcrumb {
  padding: 8px 15px;
  margin-bottom: 18px;
  list-style: none;
  background-color: #f5f5f5;
  border-radius: 2px;
}
.breadcrumb > li {
  display: inline-block;
}
.breadcrumb > li + li:before {
  content: "/\00a0";
  padding: 0 5px;
  color: #5e5e5e;
}
.breadcrumb > .active {
  color: #777777;
}
.pagination {
  display: inline-block;
  padding-left: 0;
  margin: 18px 0;
  border-radius: 2px;
}
.pagination > li {
  display: inline;
}
.pagination > li > a,
.pagination > li > span {
  position: relative;
  float: left;
  padding: 6px 12px;
  line-height: 1.42857143;
  text-decoration: none;
  color: #337ab7;
  background-color: #fff;
  border: 1px solid #ddd;
  margin-left: -1px;
}
.pagination > li:first-child > a,
.pagination > li:first-child > span {
  margin-left: 0;
  border-bottom-left-radius: 2px;
  border-top-left-radius: 2px;
}
.pagination > li:last-child > a,
.pagination > li:last-child > span {
  border-bottom-right-radius: 2px;
  border-top-right-radius: 2px;
}
.pagination > li > a:hover,
.pagination > li > span:hover,
.pagination > li > a:focus,
.pagination > li > span:focus {
  z-index: 2;
  color: #23527c;
  background-color: #eeeeee;
  border-color: #ddd;
}
.pagination > .active > a,
.pagination > .active > span,
.pagination > .active > a:hover,
.pagination > .active > span:hover,
.pagination > .active > a:focus,
.pagination > .active > span:focus {
  z-index: 3;
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
  cursor: default;
}
.pagination > .disabled > span,
.pagination > .disabled > span:hover,
.pagination > .disabled > span:focus,
.pagination > .disabled > a,
.pagination > .disabled > a:hover,
.pagination > .disabled > a:focus {
  color: #777777;
  background-color: #fff;
  border-color: #ddd;
  cursor: not-allowed;
}
.pagination-lg > li > a,
.pagination-lg > li > span {
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
}
.pagination-lg > li:first-child > a,
.pagination-lg > li:first-child > span {
  border-bottom-left-radius: 3px;
  border-top-left-radius: 3px;
}
.pagination-lg > li:last-child > a,
.pagination-lg > li:last-child > span {
  border-bottom-right-radius: 3px;
  border-top-right-radius: 3px;
}
.pagination-sm > li > a,
.pagination-sm > li > span {
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
}
.pagination-sm > li:first-child > a,
.pagination-sm > li:first-child > span {
  border-bottom-left-radius: 1px;
  border-top-left-radius: 1px;
}
.pagination-sm > li:last-child > a,
.pagination-sm > li:last-child > span {
  border-bottom-right-radius: 1px;
  border-top-right-radius: 1px;
}
.pager {
  padding-left: 0;
  margin: 18px 0;
  list-style: none;
  text-align: center;
}
.pager li {
  display: inline;
}
.pager li > a,
.pager li > span {
  display: inline-block;
  padding: 5px 14px;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 15px;
}
.pager li > a:hover,
.pager li > a:focus {
  text-decoration: none;
  background-color: #eeeeee;
}
.pager .next > a,
.pager .next > span {
  float: right;
}
.pager .previous > a,
.pager .previous > span {
  float: left;
}
.pager .disabled > a,
.pager .disabled > a:hover,
.pager .disabled > a:focus,
.pager .disabled > span {
  color: #777777;
  background-color: #fff;
  cursor: not-allowed;
}
.label {
  display: inline;
  padding: .2em .6em .3em;
  font-size: 75%;
  font-weight: bold;
  line-height: 1;
  color: #fff;
  text-align: center;
  white-space: nowrap;
  vertical-align: baseline;
  border-radius: .25em;
}
a.label:hover,
a.label:focus {
  color: #fff;
  text-decoration: none;
  cursor: pointer;
}
.label:empty {
  display: none;
}
.btn .label {
  position: relative;
  top: -1px;
}
.label-default {
  background-color: #777777;
}
.label-default[href]:hover,
.label-default[href]:focus {
  background-color: #5e5e5e;
}
.label-primary {
  background-color: #337ab7;
}
.label-primary[href]:hover,
.label-primary[href]:focus {
  background-color: #286090;
}
.label-success {
  background-color: #5cb85c;
}
.label-success[href]:hover,
.label-success[href]:focus {
  background-color: #449d44;
}
.label-info {
  background-color: #5bc0de;
}
.label-info[href]:hover,
.label-info[href]:focus {
  background-color: #31b0d5;
}
.label-warning {
  background-color: #f0ad4e;
}
.label-warning[href]:hover,
.label-warning[href]:focus {
  background-color: #ec971f;
}
.label-danger {
  background-color: #d9534f;
}
.label-danger[href]:hover,
.label-danger[href]:focus {
  background-color: #c9302c;
}
.badge {
  display: inline-block;
  min-width: 10px;
  padding: 3px 7px;
  font-size: 12px;
  font-weight: bold;
  color: #fff;
  line-height: 1;
  vertical-align: middle;
  white-space: nowrap;
  text-align: center;
  background-color: #777777;
  border-radius: 10px;
}
.badge:empty {
  display: none;
}
.btn .badge {
  position: relative;
  top: -1px;
}
.btn-xs .badge,
.btn-group-xs > .btn .badge {
  top: 0;
  padding: 1px 5px;
}
a.badge:hover,
a.badge:focus {
  color: #fff;
  text-decoration: none;
  cursor: pointer;
}
.list-group-item.active > .badge,
.nav-pills > .active > a > .badge {
  color: #337ab7;
  background-color: #fff;
}
.list-group-item > .badge {
  float: right;
}
.list-group-item > .badge + .badge {
  margin-right: 5px;
}
.nav-pills > li > a > .badge {
  margin-left: 3px;
}
.jumbotron {
  padding-top: 30px;
  padding-bottom: 30px;
  margin-bottom: 30px;
  color: inherit;
  background-color: #eeeeee;
}
.jumbotron h1,
.jumbotron .h1 {
  color: inherit;
}
.jumbotron p {
  margin-bottom: 15px;
  font-size: 20px;
  font-weight: 200;
}
.jumbotron > hr {
  border-top-color: #d5d5d5;
}
.container .jumbotron,
.container-fluid .jumbotron {
  border-radius: 3px;
  padding-left: 0px;
  padding-right: 0px;
}
.jumbotron .container {
  max-width: 100%;
}
@media screen and (min-width: 768px) {
  .jumbotron {
    padding-top: 48px;
    padding-bottom: 48px;
  }
  .container .jumbotron,
  .container-fluid .jumbotron {
    padding-left: 60px;
    padding-right: 60px;
  }
  .jumbotron h1,
  .jumbotron .h1 {
    font-size: 59px;
  }
}
.thumbnail {
  display: block;
  padding: 4px;
  margin-bottom: 18px;
  line-height: 1.42857143;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 2px;
  -webkit-transition: border 0.2s ease-in-out;
  -o-transition: border 0.2s ease-in-out;
  transition: border 0.2s ease-in-out;
}
.thumbnail > img,
.thumbnail a > img {
  margin-left: auto;
  margin-right: auto;
}
a.thumbnail:hover,
a.thumbnail:focus,
a.thumbnail.active {
  border-color: #337ab7;
}
.thumbnail .caption {
  padding: 9px;
  color: #000;
}
.alert {
  padding: 15px;
  margin-bottom: 18px;
  border: 1px solid transparent;
  border-radius: 2px;
}
.alert h4 {
  margin-top: 0;
  color: inherit;
}
.alert .alert-link {
  font-weight: bold;
}
.alert > p,
.alert > ul {
  margin-bottom: 0;
}
.alert > p + p {
  margin-top: 5px;
}
.alert-dismissable,
.alert-dismissible {
  padding-right: 35px;
}
.alert-dismissable .close,
.alert-dismissible .close {
  position: relative;
  top: -2px;
  right: -21px;
  color: inherit;
}
.alert-success {
  background-color: #dff0d8;
  border-color: #d6e9c6;
  color: #3c763d;
}
.alert-success hr {
  border-top-color: #c9e2b3;
}
.alert-success .alert-link {
  color: #2b542c;
}
.alert-info {
  background-color: #d9edf7;
  border-color: #bce8f1;
  color: #31708f;
}
.alert-info hr {
  border-top-color: #a6e1ec;
}
.alert-info .alert-link {
  color: #245269;
}
.alert-warning {
  background-color: #fcf8e3;
  border-color: #faebcc;
  color: #8a6d3b;
}
.alert-warning hr {
  border-top-color: #f7e1b5;
}
.alert-warning .alert-link {
  color: #66512c;
}
.alert-danger {
  background-color: #f2dede;
  border-color: #ebccd1;
  color: #a94442;
}
.alert-danger hr {
  border-top-color: #e4b9c0;
}
.alert-danger .alert-link {
  color: #843534;
}
@-webkit-keyframes progress-bar-stripes {
  from {
    background-position: 40px 0;
  }
  to {
    background-position: 0 0;
  }
}
@keyframes progress-bar-stripes {
  from {
    background-position: 40px 0;
  }
  to {
    background-position: 0 0;
  }
}
.progress {
  overflow: hidden;
  height: 18px;
  margin-bottom: 18px;
  background-color: #f5f5f5;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
  box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
}
.progress-bar {
  float: left;
  width: 0%;
  height: 100%;
  font-size: 12px;
  line-height: 18px;
  color: #fff;
  text-align: center;
  background-color: #337ab7;
  -webkit-box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.15);
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.15);
  -webkit-transition: width 0.6s ease;
  -o-transition: width 0.6s ease;
  transition: width 0.6s ease;
}
.progress-striped .progress-bar,
.progress-bar-striped {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-size: 40px 40px;
}
.progress.active .progress-bar,
.progress-bar.active {
  -webkit-animation: progress-bar-stripes 2s linear infinite;
  -o-animation: progress-bar-stripes 2s linear infinite;
  animation: progress-bar-stripes 2s linear infinite;
}
.progress-bar-success {
  background-color: #5cb85c;
}
.progress-striped .progress-bar-success {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-info {
  background-color: #5bc0de;
}
.progress-striped .progress-bar-info {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-warning {
  background-color: #f0ad4e;
}
.progress-striped .progress-bar-warning {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-danger {
  background-color: #d9534f;
}
.progress-striped .progress-bar-danger {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.media {
  margin-top: 15px;
}
.media:first-child {
  margin-top: 0;
}
.media,
.media-body {
  zoom: 1;
  overflow: hidden;
}
.media-body {
  width: 10000px;
}
.media-object {
  display: block;
}
.media-object.img-thumbnail {
  max-width: none;
}
.media-right,
.media > .pull-right {
  padding-left: 10px;
}
.media-left,
.media > .pull-left {
  padding-right: 10px;
}
.media-left,
.media-right,
.media-body {
  display: table-cell;
  vertical-align: top;
}
.media-middle {
  vertical-align: middle;
}
.media-bottom {
  vertical-align: bottom;
}
.media-heading {
  margin-top: 0;
  margin-bottom: 5px;
}
.media-list {
  padding-left: 0;
  list-style: none;
}
.list-group {
  margin-bottom: 20px;
  padding-left: 0;
}
.list-group-item {
  position: relative;
  display: block;
  padding: 10px 15px;
  margin-bottom: -1px;
  background-color: #fff;
  border: 1px solid #ddd;
}
.list-group-item:first-child {
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
}
.list-group-item:last-child {
  margin-bottom: 0;
  border-bottom-right-radius: 2px;
  border-bottom-left-radius: 2px;
}
a.list-group-item,
button.list-group-item {
  color: #555;
}
a.list-group-item .list-group-item-heading,
button.list-group-item .list-group-item-heading {
  color: #333;
}
a.list-group-item:hover,
button.list-group-item:hover,
a.list-group-item:focus,
button.list-group-item:focus {
  text-decoration: none;
  color: #555;
  background-color: #f5f5f5;
}
button.list-group-item {
  width: 100%;
  text-align: left;
}
.list-group-item.disabled,
.list-group-item.disabled:hover,
.list-group-item.disabled:focus {
  background-color: #eeeeee;
  color: #777777;
  cursor: not-allowed;
}
.list-group-item.disabled .list-group-item-heading,
.list-group-item.disabled:hover .list-group-item-heading,
.list-group-item.disabled:focus .list-group-item-heading {
  color: inherit;
}
.list-group-item.disabled .list-group-item-text,
.list-group-item.disabled:hover .list-group-item-text,
.list-group-item.disabled:focus .list-group-item-text {
  color: #777777;
}
.list-group-item.active,
.list-group-item.active:hover,
.list-group-item.active:focus {
  z-index: 2;
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
}
.list-group-item.active .list-group-item-heading,
.list-group-item.active:hover .list-group-item-heading,
.list-group-item.active:focus .list-group-item-heading,
.list-group-item.active .list-group-item-heading > small,
.list-group-item.active:hover .list-group-item-heading > small,
.list-group-item.active:focus .list-group-item-heading > small,
.list-group-item.active .list-group-item-heading > .small,
.list-group-item.active:hover .list-group-item-heading > .small,
.list-group-item.active:focus .list-group-item-heading > .small {
  color: inherit;
}
.list-group-item.active .list-group-item-text,
.list-group-item.active:hover .list-group-item-text,
.list-group-item.active:focus .list-group-item-text {
  color: #c7ddef;
}
.list-group-item-success {
  color: #3c763d;
  background-color: #dff0d8;
}
a.list-group-item-success,
button.list-group-item-success {
  color: #3c763d;
}
a.list-group-item-success .list-group-item-heading,
button.list-group-item-success .list-group-item-heading {
  color: inherit;
}
a.list-group-item-success:hover,
button.list-group-item-success:hover,
a.list-group-item-success:focus,
button.list-group-item-success:focus {
  color: #3c763d;
  background-color: #d0e9c6;
}
a.list-group-item-success.active,
button.list-group-item-success.active,
a.list-group-item-success.active:hover,
button.list-group-item-success.active:hover,
a.list-group-item-success.active:focus,
button.list-group-item-success.active:focus {
  color: #fff;
  background-color: #3c763d;
  border-color: #3c763d;
}
.list-group-item-info {
  color: #31708f;
  background-color: #d9edf7;
}
a.list-group-item-info,
button.list-group-item-info {
  color: #31708f;
}
a.list-group-item-info .list-group-item-heading,
button.list-group-item-info .list-group-item-heading {
  color: inherit;
}
a.list-group-item-info:hover,
button.list-group-item-info:hover,
a.list-group-item-info:focus,
button.list-group-item-info:focus {
  color: #31708f;
  background-color: #c4e3f3;
}
a.list-group-item-info.active,
button.list-group-item-info.active,
a.list-group-item-info.active:hover,
button.list-group-item-info.active:hover,
a.list-group-item-info.active:focus,
button.list-group-item-info.active:focus {
  color: #fff;
  background-color: #31708f;
  border-color: #31708f;
}
.list-group-item-warning {
  color: #8a6d3b;
  background-color: #fcf8e3;
}
a.list-group-item-warning,
button.list-group-item-warning {
  color: #8a6d3b;
}
a.list-group-item-warning .list-group-item-heading,
button.list-group-item-warning .list-group-item-heading {
  color: inherit;
}
a.list-group-item-warning:hover,
button.list-group-item-warning:hover,
a.list-group-item-warning:focus,
button.list-group-item-warning:focus {
  color: #8a6d3b;
  background-color: #faf2cc;
}
a.list-group-item-warning.active,
button.list-group-item-warning.active,
a.list-group-item-warning.active:hover,
button.list-group-item-warning.active:hover,
a.list-group-item-warning.active:focus,
button.list-group-item-warning.active:focus {
  color: #fff;
  background-color: #8a6d3b;
  border-color: #8a6d3b;
}
.list-group-item-danger {
  color: #a94442;
  background-color: #f2dede;
}
a.list-group-item-danger,
button.list-group-item-danger {
  color: #a94442;
}
a.list-group-item-danger .list-group-item-heading,
button.list-group-item-danger .list-group-item-heading {
  color: inherit;
}
a.list-group-item-danger:hover,
button.list-group-item-danger:hover,
a.list-group-item-danger:focus,
button.list-group-item-danger:focus {
  color: #a94442;
  background-color: #ebcccc;
}
a.list-group-item-danger.active,
button.list-group-item-danger.active,
a.list-group-item-danger.active:hover,
button.list-group-item-danger.active:hover,
a.list-group-item-danger.active:focus,
button.list-group-item-danger.active:focus {
  color: #fff;
  background-color: #a94442;
  border-color: #a94442;
}
.list-group-item-heading {
  margin-top: 0;
  margin-bottom: 5px;
}
.list-group-item-text {
  margin-bottom: 0;
  line-height: 1.3;
}
.panel {
  margin-bottom: 18px;
  background-color: #fff;
  border: 1px solid transparent;
  border-radius: 2px;
  -webkit-box-shadow: 0 1px 1px rgba(0, 0, 0, 0.05);
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.05);
}
.panel-body {
  padding: 15px;
}
.panel-heading {
  padding: 10px 15px;
  border-bottom: 1px solid transparent;
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel-heading > .dropdown .dropdown-toggle {
  color: inherit;
}
.panel-title {
  margin-top: 0;
  margin-bottom: 0;
  font-size: 15px;
  color: inherit;
}
.panel-title > a,
.panel-title > small,
.panel-title > .small,
.panel-title > small > a,
.panel-title > .small > a {
  color: inherit;
}
.panel-footer {
  padding: 10px 15px;
  background-color: #f5f5f5;
  border-top: 1px solid #ddd;
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .list-group,
.panel > .panel-collapse > .list-group {
  margin-bottom: 0;
}
.panel > .list-group .list-group-item,
.panel > .panel-collapse > .list-group .list-group-item {
  border-width: 1px 0;
  border-radius: 0;
}
.panel > .list-group:first-child .list-group-item:first-child,
.panel > .panel-collapse > .list-group:first-child .list-group-item:first-child {
  border-top: 0;
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel > .list-group:last-child .list-group-item:last-child,
.panel > .panel-collapse > .list-group:last-child .list-group-item:last-child {
  border-bottom: 0;
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .panel-heading + .panel-collapse > .list-group .list-group-item:first-child {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.panel-heading + .list-group .list-group-item:first-child {
  border-top-width: 0;
}
.list-group + .panel-footer {
  border-top-width: 0;
}
.panel > .table,
.panel > .table-responsive > .table,
.panel > .panel-collapse > .table {
  margin-bottom: 0;
}
.panel > .table caption,
.panel > .table-responsive > .table caption,
.panel > .panel-collapse > .table caption {
  padding-left: 15px;
  padding-right: 15px;
}
.panel > .table:first-child,
.panel > .table-responsive:first-child > .table:first-child {
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child {
  border-top-left-radius: 1px;
  border-top-right-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child td:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child td:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child td:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child td:first-child,
.panel > .table:first-child > thead:first-child > tr:first-child th:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child th:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child th:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child th:first-child {
  border-top-left-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child td:last-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child td:last-child,
.panel > .table:first-child > tbody:first-child > tr:first-child td:last-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child td:last-child,
.panel > .table:first-child > thead:first-child > tr:first-child th:last-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child th:last-child,
.panel > .table:first-child > tbody:first-child > tr:first-child th:last-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child th:last-child {
  border-top-right-radius: 1px;
}
.panel > .table:last-child,
.panel > .table-responsive:last-child > .table:last-child {
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child {
  border-bottom-left-radius: 1px;
  border-bottom-right-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child td:first-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child td:first-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child td:first-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child td:first-child,
.panel > .table:last-child > tbody:last-child > tr:last-child th:first-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child th:first-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child th:first-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child th:first-child {
  border-bottom-left-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child td:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child td:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child td:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child td:last-child,
.panel > .table:last-child > tbody:last-child > tr:last-child th:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child th:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child th:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child th:last-child {
  border-bottom-right-radius: 1px;
}
.panel > .panel-body + .table,
.panel > .panel-body + .table-responsive,
.panel > .table + .panel-body,
.panel > .table-responsive + .panel-body {
  border-top: 1px solid #ddd;
}
.panel > .table > tbody:first-child > tr:first-child th,
.panel > .table > tbody:first-child > tr:first-child td {
  border-top: 0;
}
.panel > .table-bordered,
.panel > .table-responsive > .table-bordered {
  border: 0;
}
.panel > .table-bordered > thead > tr > th:first-child,
.panel > .table-responsive > .table-bordered > thead > tr > th:first-child,
.panel > .table-bordered > tbody > tr > th:first-child,
.panel > .table-responsive > .table-bordered > tbody > tr > th:first-child,
.panel > .table-bordered > tfoot > tr > th:first-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > th:first-child,
.panel > .table-bordered > thead > tr > td:first-child,
.panel > .table-responsive > .table-bordered > thead > tr > td:first-child,
.panel > .table-bordered > tbody > tr > td:first-child,
.panel > .table-responsive > .table-bordered > tbody > tr > td:first-child,
.panel > .table-bordered > tfoot > tr > td:first-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > td:first-child {
  border-left: 0;
}
.panel > .table-bordered > thead > tr > th:last-child,
.panel > .table-responsive > .table-bordered > thead > tr > th:last-child,
.panel > .table-bordered > tbody > tr > th:last-child,
.panel > .table-responsive > .table-bordered > tbody > tr > th:last-child,
.panel > .table-bordered > tfoot > tr > th:last-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > th:last-child,
.panel > .table-bordered > thead > tr > td:last-child,
.panel > .table-responsive > .table-bordered > thead > tr > td:last-child,
.panel > .table-bordered > tbody > tr > td:last-child,
.panel > .table-responsive > .table-bordered > tbody > tr > td:last-child,
.panel > .table-bordered > tfoot > tr > td:last-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > td:last-child {
  border-right: 0;
}
.panel > .table-bordered > thead > tr:first-child > td,
.panel > .table-responsive > .table-bordered > thead > tr:first-child > td,
.panel > .table-bordered > tbody > tr:first-child > td,
.panel > .table-responsive > .table-bordered > tbody > tr:first-child > td,
.panel > .table-bordered > thead > tr:first-child > th,
.panel > .table-responsive > .table-bordered > thead > tr:first-child > th,
.panel > .table-bordered > tbody > tr:first-child > th,
.panel > .table-responsive > .table-bordered > tbody > tr:first-child > th {
  border-bottom: 0;
}
.panel > .table-bordered > tbody > tr:last-child > td,
.panel > .table-responsive > .table-bordered > tbody > tr:last-child > td,
.panel > .table-bordered > tfoot > tr:last-child > td,
.panel > .table-responsive > .table-bordered > tfoot > tr:last-child > td,
.panel > .table-bordered > tbody > tr:last-child > th,
.panel > .table-responsive > .table-bordered > tbody > tr:last-child > th,
.panel > .table-bordered > tfoot > tr:last-child > th,
.panel > .table-responsive > .table-bordered > tfoot > tr:last-child > th {
  border-bottom: 0;
}
.panel > .table-responsive {
  border: 0;
  margin-bottom: 0;
}
.panel-group {
  margin-bottom: 18px;
}
.panel-group .panel {
  margin-bottom: 0;
  border-radius: 2px;
}
.panel-group .panel + .panel {
  margin-top: 5px;
}
.panel-group .panel-heading {
  border-bottom: 0;
}
.panel-group .panel-heading + .panel-collapse > .panel-body,
.panel-group .panel-heading + .panel-collapse > .list-group {
  border-top: 1px solid #ddd;
}
.panel-group .panel-footer {
  border-top: 0;
}
.panel-group .panel-footer + .panel-collapse .panel-body {
  border-bottom: 1px solid #ddd;
}
.panel-default {
  border-color: #ddd;
}
.panel-default > .panel-heading {
  color: #333333;
  background-color: #f5f5f5;
  border-color: #ddd;
}
.panel-default > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #ddd;
}
.panel-default > .panel-heading .badge {
  color: #f5f5f5;
  background-color: #333333;
}
.panel-default > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #ddd;
}
.panel-primary {
  border-color: #337ab7;
}
.panel-primary > .panel-heading {
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
}
.panel-primary > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #337ab7;
}
.panel-primary > .panel-heading .badge {
  color: #337ab7;
  background-color: #fff;
}
.panel-primary > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #337ab7;
}
.panel-success {
  border-color: #d6e9c6;
}
.panel-success > .panel-heading {
  color: #3c763d;
  background-color: #dff0d8;
  border-color: #d6e9c6;
}
.panel-success > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #d6e9c6;
}
.panel-success > .panel-heading .badge {
  color: #dff0d8;
  background-color: #3c763d;
}
.panel-success > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #d6e9c6;
}
.panel-info {
  border-color: #bce8f1;
}
.panel-info > .panel-heading {
  color: #31708f;
  background-color: #d9edf7;
  border-color: #bce8f1;
}
.panel-info > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #bce8f1;
}
.panel-info > .panel-heading .badge {
  color: #d9edf7;
  background-color: #31708f;
}
.panel-info > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #bce8f1;
}
.panel-warning {
  border-color: #faebcc;
}
.panel-warning > .panel-heading {
  color: #8a6d3b;
  background-color: #fcf8e3;
  border-color: #faebcc;
}
.panel-warning > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #faebcc;
}
.panel-warning > .panel-heading .badge {
  color: #fcf8e3;
  background-color: #8a6d3b;
}
.panel-warning > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #faebcc;
}
.panel-danger {
  border-color: #ebccd1;
}
.panel-danger > .panel-heading {
  color: #a94442;
  background-color: #f2dede;
  border-color: #ebccd1;
}
.panel-danger > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #ebccd1;
}
.panel-danger > .panel-heading .badge {
  color: #f2dede;
  background-color: #a94442;
}
.panel-danger > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #ebccd1;
}
.embed-responsive {
  position: relative;
  display: block;
  height: 0;
  padding: 0;
  overflow: hidden;
}
.embed-responsive .embed-responsive-item,
.embed-responsive iframe,
.embed-responsive embed,
.embed-responsive object,
.embed-responsive video {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  height: 100%;
  width: 100%;
  border: 0;
}
.embed-responsive-16by9 {
  padding-bottom: 56.25%;
}
.embed-responsive-4by3 {
  padding-bottom: 75%;
}
.well {
  min-height: 20px;
  padding: 19px;
  margin-bottom: 20px;
  background-color: #f5f5f5;
  border: 1px solid #e3e3e3;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.05);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.05);
}
.well blockquote {
  border-color: #ddd;
  border-color: rgba(0, 0, 0, 0.15);
}
.well-lg {
  padding: 24px;
  border-radius: 3px;
}
.well-sm {
  padding: 9px;
  border-radius: 1px;
}
.close {
  float: right;
  font-size: 19.5px;
  font-weight: bold;
  line-height: 1;
  color: #000;
  text-shadow: 0 1px 0 #fff;
  opacity: 0.2;
  filter: alpha(opacity=20);
}
.close:hover,
.close:focus {
  color: #000;
  text-decoration: none;
  cursor: pointer;
  opacity: 0.5;
  filter: alpha(opacity=50);
}
button.close {
  padding: 0;
  cursor: pointer;
  background: transparent;
  border: 0;
  -webkit-appearance: none;
}
.modal-open {
  overflow: hidden;
}
.modal {
  display: none;
  overflow: hidden;
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1050;
  -webkit-overflow-scrolling: touch;
  outline: 0;
}
.modal.fade .modal-dialog {
  -webkit-transform: translate(0, -25%);
  -ms-transform: translate(0, -25%);
  -o-transform: translate(0, -25%);
  transform: translate(0, -25%);
  -webkit-transition: -webkit-transform 0.3s ease-out;
  -moz-transition: -moz-transform 0.3s ease-out;
  -o-transition: -o-transform 0.3s ease-out;
  transition: transform 0.3s ease-out;
}
.modal.in .modal-dialog {
  -webkit-transform: translate(0, 0);
  -ms-transform: translate(0, 0);
  -o-transform: translate(0, 0);
  transform: translate(0, 0);
}
.modal-open .modal {
  overflow-x: hidden;
  overflow-y: auto;
}
.modal-dialog {
  position: relative;
  width: auto;
  margin: 10px;
}
.modal-content {
  position: relative;
  background-color: #fff;
  border: 1px solid #999;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 3px;
  -webkit-box-shadow: 0 3px 9px rgba(0, 0, 0, 0.5);
  box-shadow: 0 3px 9px rgba(0, 0, 0, 0.5);
  background-clip: padding-box;
  outline: 0;
}
.modal-backdrop {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1040;
  background-color: #000;
}
.modal-backdrop.fade {
  opacity: 0;
  filter: alpha(opacity=0);
}
.modal-backdrop.in {
  opacity: 0.5;
  filter: alpha(opacity=50);
}
.modal-header {
  padding: 15px;
  border-bottom: 1px solid #e5e5e5;
}
.modal-header .close {
  margin-top: -2px;
}
.modal-title {
  margin: 0;
  line-height: 1.42857143;
}
.modal-body {
  position: relative;
  padding: 15px;
}
.modal-footer {
  padding: 15px;
  text-align: right;
  border-top: 1px solid #e5e5e5;
}
.modal-footer .btn + .btn {
  margin-left: 5px;
  margin-bottom: 0;
}
.modal-footer .btn-group .btn + .btn {
  margin-left: -1px;
}
.modal-footer .btn-block + .btn-block {
  margin-left: 0;
}
.modal-scrollbar-measure {
  position: absolute;
  top: -9999px;
  width: 50px;
  height: 50px;
  overflow: scroll;
}
@media (min-width: 768px) {
  .modal-dialog {
    width: 600px;
    margin: 30px auto;
  }
  .modal-content {
    -webkit-box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
  }
  .modal-sm {
    width: 300px;
  }
}
@media (min-width: 992px) {
  .modal-lg {
    width: 900px;
  }
}
.tooltip {
  position: absolute;
  z-index: 1070;
  display: block;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-style: normal;
  font-weight: normal;
  letter-spacing: normal;
  line-break: auto;
  line-height: 1.42857143;
  text-align: left;
  text-align: start;
  text-decoration: none;
  text-shadow: none;
  text-transform: none;
  white-space: normal;
  word-break: normal;
  word-spacing: normal;
  word-wrap: normal;
  font-size: 12px;
  opacity: 0;
  filter: alpha(opacity=0);
}
.tooltip.in {
  opacity: 0.9;
  filter: alpha(opacity=90);
}
.tooltip.top {
  margin-top: -3px;
  padding: 5px 0;
}
.tooltip.right {
  margin-left: 3px;
  padding: 0 5px;
}
.tooltip.bottom {
  margin-top: 3px;
  padding: 5px 0;
}
.tooltip.left {
  margin-left: -3px;
  padding: 0 5px;
}
.tooltip-inner {
  max-width: 200px;
  padding: 3px 8px;
  color: #fff;
  text-align: center;
  background-color: #000;
  border-radius: 2px;
}
.tooltip-arrow {
  position: absolute;
  width: 0;
  height: 0;
  border-color: transparent;
  border-style: solid;
}
.tooltip.top .tooltip-arrow {
  bottom: 0;
  left: 50%;
  margin-left: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.top-left .tooltip-arrow {
  bottom: 0;
  right: 5px;
  margin-bottom: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.top-right .tooltip-arrow {
  bottom: 0;
  left: 5px;
  margin-bottom: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.right .tooltip-arrow {
  top: 50%;
  left: 0;
  margin-top: -5px;
  border-width: 5px 5px 5px 0;
  border-right-color: #000;
}
.tooltip.left .tooltip-arrow {
  top: 50%;
  right: 0;
  margin-top: -5px;
  border-width: 5px 0 5px 5px;
  border-left-color: #000;
}
.tooltip.bottom .tooltip-arrow {
  top: 0;
  left: 50%;
  margin-left: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.tooltip.bottom-left .tooltip-arrow {
  top: 0;
  right: 5px;
  margin-top: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.tooltip.bottom-right .tooltip-arrow {
  top: 0;
  left: 5px;
  margin-top: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.popover {
  position: absolute;
  top: 0;
  left: 0;
  z-index: 1060;
  display: none;
  max-width: 276px;
  padding: 1px;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-style: normal;
  font-weight: normal;
  letter-spacing: normal;
  line-break: auto;
  line-height: 1.42857143;
  text-align: left;
  text-align: start;
  text-decoration: none;
  text-shadow: none;
  text-transform: none;
  white-space: normal;
  word-break: normal;
  word-spacing: normal;
  word-wrap: normal;
  font-size: 13px;
  background-color: #fff;
  background-clip: padding-box;
  border: 1px solid #ccc;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 3px;
  -webkit-box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
}
.popover.top {
  margin-top: -10px;
}
.popover.right {
  margin-left: 10px;
}
.popover.bottom {
  margin-top: 10px;
}
.popover.left {
  margin-left: -10px;
}
.popover-title {
  margin: 0;
  padding: 8px 14px;
  font-size: 13px;
  background-color: #f7f7f7;
  border-bottom: 1px solid #ebebeb;
  border-radius: 2px 2px 0 0;
}
.popover-content {
  padding: 9px 14px;
}
.popover > .arrow,
.popover > .arrow:after {
  position: absolute;
  display: block;
  width: 0;
  height: 0;
  border-color: transparent;
  border-style: solid;
}
.popover > .arrow {
  border-width: 11px;
}
.popover > .arrow:after {
  border-width: 10px;
  content: "";
}
.popover.top > .arrow {
  left: 50%;
  margin-left: -11px;
  border-bottom-width: 0;
  border-top-color: #999999;
  border-top-color: rgba(0, 0, 0, 0.25);
  bottom: -11px;
}
.popover.top > .arrow:after {
  content: " ";
  bottom: 1px;
  margin-left: -10px;
  border-bottom-width: 0;
  border-top-color: #fff;
}
.popover.right > .arrow {
  top: 50%;
  left: -11px;
  margin-top: -11px;
  border-left-width: 0;
  border-right-color: #999999;
  border-right-color: rgba(0, 0, 0, 0.25);
}
.popover.right > .arrow:after {
  content: " ";
  left: 1px;
  bottom: -10px;
  border-left-width: 0;
  border-right-color: #fff;
}
.popover.bottom > .arrow {
  left: 50%;
  margin-left: -11px;
  border-top-width: 0;
  border-bottom-color: #999999;
  border-bottom-color: rgba(0, 0, 0, 0.25);
  top: -11px;
}
.popover.bottom > .arrow:after {
  content: " ";
  top: 1px;
  margin-left: -10px;
  border-top-width: 0;
  border-bottom-color: #fff;
}
.popover.left > .arrow {
  top: 50%;
  right: -11px;
  margin-top: -11px;
  border-right-width: 0;
  border-left-color: #999999;
  border-left-color: rgba(0, 0, 0, 0.25);
}
.popover.left > .arrow:after {
  content: " ";
  right: 1px;
  border-right-width: 0;
  border-left-color: #fff;
  bottom: -10px;
}
.carousel {
  position: relative;
}
.carousel-inner {
  position: relative;
  overflow: hidden;
  width: 100%;
}
.carousel-inner > .item {
  display: none;
  position: relative;
  -webkit-transition: 0.6s ease-in-out left;
  -o-transition: 0.6s ease-in-out left;
  transition: 0.6s ease-in-out left;
}
.carousel-inner > .item > img,
.carousel-inner > .item > a > img {
  line-height: 1;
}
@media all and (transform-3d), (-webkit-transform-3d) {
  .carousel-inner > .item {
    -webkit-transition: -webkit-transform 0.6s ease-in-out;
    -moz-transition: -moz-transform 0.6s ease-in-out;
    -o-transition: -o-transform 0.6s ease-in-out;
    transition: transform 0.6s ease-in-out;
    -webkit-backface-visibility: hidden;
    -moz-backface-visibility: hidden;
    backface-visibility: hidden;
    -webkit-perspective: 1000px;
    -moz-perspective: 1000px;
    perspective: 1000px;
  }
  .carousel-inner > .item.next,
  .carousel-inner > .item.active.right {
    -webkit-transform: translate3d(100%, 0, 0);
    transform: translate3d(100%, 0, 0);
    left: 0;
  }
  .carousel-inner > .item.prev,
  .carousel-inner > .item.active.left {
    -webkit-transform: translate3d(-100%, 0, 0);
    transform: translate3d(-100%, 0, 0);
    left: 0;
  }
  .carousel-inner > .item.next.left,
  .carousel-inner > .item.prev.right,
  .carousel-inner > .item.active {
    -webkit-transform: translate3d(0, 0, 0);
    transform: translate3d(0, 0, 0);
    left: 0;
  }
}
.carousel-inner > .active,
.carousel-inner > .next,
.carousel-inner > .prev {
  display: block;
}
.carousel-inner > .active {
  left: 0;
}
.carousel-inner > .next,
.carousel-inner > .prev {
  position: absolute;
  top: 0;
  width: 100%;
}
.carousel-inner > .next {
  left: 100%;
}
.carousel-inner > .prev {
  left: -100%;
}
.carousel-inner > .next.left,
.carousel-inner > .prev.right {
  left: 0;
}
.carousel-inner > .active.left {
  left: -100%;
}
.carousel-inner > .active.right {
  left: 100%;
}
.carousel-control {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  width: 15%;
  opacity: 0.5;
  filter: alpha(opacity=50);
  font-size: 20px;
  color: #fff;
  text-align: center;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.6);
  background-color: rgba(0, 0, 0, 0);
}
.carousel-control.left {
  background-image: -webkit-linear-gradient(left, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-image: -o-linear-gradient(left, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-image: linear-gradient(to right, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#80000000', endColorstr='#00000000', GradientType=1);
}
.carousel-control.right {
  left: auto;
  right: 0;
  background-image: -webkit-linear-gradient(left, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-image: -o-linear-gradient(left, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-image: linear-gradient(to right, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#00000000', endColorstr='#80000000', GradientType=1);
}
.carousel-control:hover,
.carousel-control:focus {
  outline: 0;
  color: #fff;
  text-decoration: none;
  opacity: 0.9;
  filter: alpha(opacity=90);
}
.carousel-control .icon-prev,
.carousel-control .icon-next,
.carousel-control .glyphicon-chevron-left,
.carousel-control .glyphicon-chevron-right {
  position: absolute;
  top: 50%;
  margin-top: -10px;
  z-index: 5;
  display: inline-block;
}
.carousel-control .icon-prev,
.carousel-control .glyphicon-chevron-left {
  left: 50%;
  margin-left: -10px;
}
.carousel-control .icon-next,
.carousel-control .glyphicon-chevron-right {
  right: 50%;
  margin-right: -10px;
}
.carousel-control .icon-prev,
.carousel-control .icon-next {
  width: 20px;
  height: 20px;
  line-height: 1;
  font-family: serif;
}
.carousel-control .icon-prev:before {
  content: '\2039';
}
.carousel-control .icon-next:before {
  content: '\203a';
}
.carousel-indicators {
  position: absolute;
  bottom: 10px;
  left: 50%;
  z-index: 15;
  width: 60%;
  margin-left: -30%;
  padding-left: 0;
  list-style: none;
  text-align: center;
}
.carousel-indicators li {
  display: inline-block;
  width: 10px;
  height: 10px;
  margin: 1px;
  text-indent: -999px;
  border: 1px solid #fff;
  border-radius: 10px;
  cursor: pointer;
  background-color: #000 \9;
  background-color: rgba(0, 0, 0, 0);
}
.carousel-indicators .active {
  margin: 0;
  width: 12px;
  height: 12px;
  background-color: #fff;
}
.carousel-caption {
  position: absolute;
  left: 15%;
  right: 15%;
  bottom: 20px;
  z-index: 10;
  padding-top: 20px;
  padding-bottom: 20px;
  color: #fff;
  text-align: center;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.6);
}
.carousel-caption .btn {
  text-shadow: none;
}
@media screen and (min-width: 768px) {
  .carousel-control .glyphicon-chevron-left,
  .carousel-control .glyphicon-chevron-right,
  .carousel-control .icon-prev,
  .carousel-control .icon-next {
    width: 30px;
    height: 30px;
    margin-top: -10px;
    font-size: 30px;
  }
  .carousel-control .glyphicon-chevron-left,
  .carousel-control .icon-prev {
    margin-left: -10px;
  }
  .carousel-control .glyphicon-chevron-right,
  .carousel-control .icon-next {
    margin-right: -10px;
  }
  .carousel-caption {
    left: 20%;
    right: 20%;
    padding-bottom: 30px;
  }
  .carousel-indicators {
    bottom: 20px;
  }
}
.clearfix:before,
.clearfix:after,
.dl-horizontal dd:before,
.dl-horizontal dd:after,
.container:before,
.container:after,
.container-fluid:before,
.container-fluid:after,
.row:before,
.row:after,
.form-horizontal .form-group:before,
.form-horizontal .form-group:after,
.btn-toolbar:before,
.btn-toolbar:after,
.btn-group-vertical > .btn-group:before,
.btn-group-vertical > .btn-group:after,
.nav:before,
.nav:after,
.navbar:before,
.navbar:after,
.navbar-header:before,
.navbar-header:after,
.navbar-collapse:before,
.navbar-collapse:after,
.pager:before,
.pager:after,
.panel-body:before,
.panel-body:after,
.modal-header:before,
.modal-header:after,
.modal-footer:before,
.modal-footer:after,
.item_buttons:before,
.item_buttons:after {
  content: " ";
  display: table;
}
.clearfix:after,
.dl-horizontal dd:after,
.container:after,
.container-fluid:after,
.row:after,
.form-horizontal .form-group:after,
.btn-toolbar:after,
.btn-group-vertical > .btn-group:after,
.nav:after,
.navbar:after,
.navbar-header:after,
.navbar-collapse:after,
.pager:after,
.panel-body:after,
.modal-header:after,
.modal-footer:after,
.item_buttons:after {
  clear: both;
}
.center-block {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.pull-right {
  float: right !important;
}
.pull-left {
  float: left !important;
}
.hide {
  display: none !important;
}
.show {
  display: block !important;
}
.invisible {
  visibility: hidden;
}
.text-hide {
  font: 0/0 a;
  color: transparent;
  text-shadow: none;
  background-color: transparent;
  border: 0;
}
.hidden {
  display: none !important;
}
.affix {
  position: fixed;
}
@-ms-viewport {
  width: device-width;
}
.visible-xs,
.visible-sm,
.visible-md,
.visible-lg {
  display: none !important;
}
.visible-xs-block,
.visible-xs-inline,
.visible-xs-inline-block,
.visible-sm-block,
.visible-sm-inline,
.visible-sm-inline-block,
.visible-md-block,
.visible-md-inline,
.visible-md-inline-block,
.visible-lg-block,
.visible-lg-inline,
.visible-lg-inline-block {
  display: none !important;
}
@media (max-width: 767px) {
  .visible-xs {
    display: block !important;
  }
  table.visible-xs {
    display: table !important;
  }
  tr.visible-xs {
    display: table-row !important;
  }
  th.visible-xs,
  td.visible-xs {
    display: table-cell !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-block {
    display: block !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-inline {
    display: inline !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm {
    display: block !important;
  }
  table.visible-sm {
    display: table !important;
  }
  tr.visible-sm {
    display: table-row !important;
  }
  th.visible-sm,
  td.visible-sm {
    display: table-cell !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-block {
    display: block !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-inline {
    display: inline !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md {
    display: block !important;
  }
  table.visible-md {
    display: table !important;
  }
  tr.visible-md {
    display: table-row !important;
  }
  th.visible-md,
  td.visible-md {
    display: table-cell !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-block {
    display: block !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-inline {
    display: inline !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg {
    display: block !important;
  }
  table.visible-lg {
    display: table !important;
  }
  tr.visible-lg {
    display: table-row !important;
  }
  th.visible-lg,
  td.visible-lg {
    display: table-cell !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-block {
    display: block !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-inline {
    display: inline !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-inline-block {
    display: inline-block !important;
  }
}
@media (max-width: 767px) {
  .hidden-xs {
    display: none !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .hidden-sm {
    display: none !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .hidden-md {
    display: none !important;
  }
}
@media (min-width: 1200px) {
  .hidden-lg {
    display: none !important;
  }
}
.visible-print {
  display: none !important;
}
@media print {
  .visible-print {
    display: block !important;
  }
  table.visible-print {
    display: table !important;
  }
  tr.visible-print {
    display: table-row !important;
  }
  th.visible-print,
  td.visible-print {
    display: table-cell !important;
  }
}
.visible-print-block {
  display: none !important;
}
@media print {
  .visible-print-block {
    display: block !important;
  }
}
.visible-print-inline {
  display: none !important;
}
@media print {
  .visible-print-inline {
    display: inline !important;
  }
}
.visible-print-inline-block {
  display: none !important;
}
@media print {
  .visible-print-inline-block {
    display: inline-block !important;
  }
}
@media print {
  .hidden-print {
    display: none !important;
  }
}
/*!
*
* Font Awesome
*
*/
/*!
 *  Font Awesome 4.2.0 by @davegandy - http://fontawesome.io - @fontawesome
 *  License - http://fontawesome.io/license (Font: SIL OFL 1.1, CSS: MIT License)
 */
/* FONT PATH
 * -------------------------- */
@font-face {
  font-family: 'FontAwesome';
  src: url('../components/font-awesome/fonts/fontawesome-webfont.eot?v=4.2.0');
  src: url('../components/font-awesome/fonts/fontawesome-webfont.eot?#iefix&v=4.2.0') format('embedded-opentype'), url('../components/font-awesome/fonts/fontawesome-webfont.woff?v=4.2.0') format('woff'), url('../components/font-awesome/fonts/fontawesome-webfont.ttf?v=4.2.0') format('truetype'), url('../components/font-awesome/fonts/fontawesome-webfont.svg?v=4.2.0#fontawesomeregular') format('svg');
  font-weight: normal;
  font-style: normal;
}
.fa {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
/* makes the font 33% larger relative to the icon container */
.fa-lg {
  font-size: 1.33333333em;
  line-height: 0.75em;
  vertical-align: -15%;
}
.fa-2x {
  font-size: 2em;
}
.fa-3x {
  font-size: 3em;
}
.fa-4x {
  font-size: 4em;
}
.fa-5x {
  font-size: 5em;
}
.fa-fw {
  width: 1.28571429em;
  text-align: center;
}
.fa-ul {
  padding-left: 0;
  margin-left: 2.14285714em;
  list-style-type: none;
}
.fa-ul > li {
  position: relative;
}
.fa-li {
  position: absolute;
  left: -2.14285714em;
  width: 2.14285714em;
  top: 0.14285714em;
  text-align: center;
}
.fa-li.fa-lg {
  left: -1.85714286em;
}
.fa-border {
  padding: .2em .25em .15em;
  border: solid 0.08em #eee;
  border-radius: .1em;
}
.pull-right {
  float: right;
}
.pull-left {
  float: left;
}
.fa.pull-left {
  margin-right: .3em;
}
.fa.pull-right {
  margin-left: .3em;
}
.fa-spin {
  -webkit-animation: fa-spin 2s infinite linear;
  animation: fa-spin 2s infinite linear;
}
@-webkit-keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(359deg);
    transform: rotate(359deg);
  }
}
@keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(359deg);
    transform: rotate(359deg);
  }
}
.fa-rotate-90 {
  filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=1);
  -webkit-transform: rotate(90deg);
  -ms-transform: rotate(90deg);
  transform: rotate(90deg);
}
.fa-rotate-180 {
  filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=2);
  -webkit-transform: rotate(180deg);
  -ms-transform: rotate(180deg);
  transform: rotate(180deg);
}
.fa-rotate-270 {
  filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=3);
  -webkit-transform: rotate(270deg);
  -ms-transform: rotate(270deg);
  transform: rotate(270deg);
}
.fa-flip-horizontal {
  filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=0, mirror=1);
  -webkit-transform: scale(-1, 1);
  -ms-transform: scale(-1, 1);
  transform: scale(-1, 1);
}
.fa-flip-vertical {
  filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=2, mirror=1);
  -webkit-transform: scale(1, -1);
  -ms-transform: scale(1, -1);
  transform: scale(1, -1);
}
:root .fa-rotate-90,
:root .fa-rotate-180,
:root .fa-rotate-270,
:root .fa-flip-horizontal,
:root .fa-flip-vertical {
  filter: none;
}
.fa-stack {
  position: relative;
  display: inline-block;
  width: 2em;
  height: 2em;
  line-height: 2em;
  vertical-align: middle;
}
.fa-stack-1x,
.fa-stack-2x {
  position: absolute;
  left: 0;
  width: 100%;
  text-align: center;
}
.fa-stack-1x {
  line-height: inherit;
}
.fa-stack-2x {
  font-size: 2em;
}
.fa-inverse {
  color: #fff;
}
/* Font Awesome uses the Unicode Private Use Area (PUA) to ensure screen
   readers do not read off random characters that represent icons */
.fa-glass:before {
  content: "\f000";
}
.fa-music:before {
  content: "\f001";
}
.fa-search:before {
  content: "\f002";
}
.fa-envelope-o:before {
  content: "\f003";
}
.fa-heart:before {
  content: "\f004";
}
.fa-star:before {
  content: "\f005";
}
.fa-star-o:before {
  content: "\f006";
}
.fa-user:before {
  content: "\f007";
}
.fa-film:before {
  content: "\f008";
}
.fa-th-large:before {
  content: "\f009";
}
.fa-th:before {
  content: "\f00a";
}
.fa-th-list:before {
  content: "\f00b";
}
.fa-check:before {
  content: "\f00c";
}
.fa-remove:before,
.fa-close:before,
.fa-times:before {
  content: "\f00d";
}
.fa-search-plus:before {
  content: "\f00e";
}
.fa-search-minus:before {
  content: "\f010";
}
.fa-power-off:before {
  content: "\f011";
}
.fa-signal:before {
  content: "\f012";
}
.fa-gear:before,
.fa-cog:before {
  content: "\f013";
}
.fa-trash-o:before {
  content: "\f014";
}
.fa-home:before {
  content: "\f015";
}
.fa-file-o:before {
  content: "\f016";
}
.fa-clock-o:before {
  content: "\f017";
}
.fa-road:before {
  content: "\f018";
}
.fa-download:before {
  content: "\f019";
}
.fa-arrow-circle-o-down:before {
  content: "\f01a";
}
.fa-arrow-circle-o-up:before {
  content: "\f01b";
}
.fa-inbox:before {
  content: "\f01c";
}
.fa-play-circle-o:before {
  content: "\f01d";
}
.fa-rotate-right:before,
.fa-repeat:before {
  content: "\f01e";
}
.fa-refresh:before {
  content: "\f021";
}
.fa-list-alt:before {
  content: "\f022";
}
.fa-lock:before {
  content: "\f023";
}
.fa-flag:before {
  content: "\f024";
}
.fa-headphones:before {
  content: "\f025";
}
.fa-volume-off:before {
  content: "\f026";
}
.fa-volume-down:before {
  content: "\f027";
}
.fa-volume-up:before {
  content: "\f028";
}
.fa-qrcode:before {
  content: "\f029";
}
.fa-barcode:before {
  content: "\f02a";
}
.fa-tag:before {
  content: "\f02b";
}
.fa-tags:before {
  content: "\f02c";
}
.fa-book:before {
  content: "\f02d";
}
.fa-bookmark:before {
  content: "\f02e";
}
.fa-print:before {
  content: "\f02f";
}
.fa-camera:before {
  content: "\f030";
}
.fa-font:before {
  content: "\f031";
}
.fa-bold:before {
  content: "\f032";
}
.fa-italic:before {
  content: "\f033";
}
.fa-text-height:before {
  content: "\f034";
}
.fa-text-width:before {
  content: "\f035";
}
.fa-align-left:before {
  content: "\f036";
}
.fa-align-center:before {
  content: "\f037";
}
.fa-align-right:before {
  content: "\f038";
}
.fa-align-justify:before {
  content: "\f039";
}
.fa-list:before {
  content: "\f03a";
}
.fa-dedent:before,
.fa-outdent:before {
  content: "\f03b";
}
.fa-indent:before {
  content: "\f03c";
}
.fa-video-camera:before {
  content: "\f03d";
}
.fa-photo:before,
.fa-image:before,
.fa-picture-o:before {
  content: "\f03e";
}
.fa-pencil:before {
  content: "\f040";
}
.fa-map-marker:before {
  content: "\f041";
}
.fa-adjust:before {
  content: "\f042";
}
.fa-tint:before {
  content: "\f043";
}
.fa-edit:before,
.fa-pencil-square-o:before {
  content: "\f044";
}
.fa-share-square-o:before {
  content: "\f045";
}
.fa-check-square-o:before {
  content: "\f046";
}
.fa-arrows:before {
  content: "\f047";
}
.fa-step-backward:before {
  content: "\f048";
}
.fa-fast-backward:before {
  content: "\f049";
}
.fa-backward:before {
  content: "\f04a";
}
.fa-play:before {
  content: "\f04b";
}
.fa-pause:before {
  content: "\f04c";
}
.fa-stop:before {
  content: "\f04d";
}
.fa-forward:before {
  content: "\f04e";
}
.fa-fast-forward:before {
  content: "\f050";
}
.fa-step-forward:before {
  content: "\f051";
}
.fa-eject:before {
  content: "\f052";
}
.fa-chevron-left:before {
  content: "\f053";
}
.fa-chevron-right:before {
  content: "\f054";
}
.fa-plus-circle:before {
  content: "\f055";
}
.fa-minus-circle:before {
  content: "\f056";
}
.fa-times-circle:before {
  content: "\f057";
}
.fa-check-circle:before {
  content: "\f058";
}
.fa-question-circle:before {
  content: "\f059";
}
.fa-info-circle:before {
  content: "\f05a";
}
.fa-crosshairs:before {
  content: "\f05b";
}
.fa-times-circle-o:before {
  content: "\f05c";
}
.fa-check-circle-o:before {
  content: "\f05d";
}
.fa-ban:before {
  content: "\f05e";
}
.fa-arrow-left:before {
  content: "\f060";
}
.fa-arrow-right:before {
  content: "\f061";
}
.fa-arrow-up:before {
  content: "\f062";
}
.fa-arrow-down:before {
  content: "\f063";
}
.fa-mail-forward:before,
.fa-share:before {
  content: "\f064";
}
.fa-expand:before {
  content: "\f065";
}
.fa-compress:before {
  content: "\f066";
}
.fa-plus:before {
  content: "\f067";
}
.fa-minus:before {
  content: "\f068";
}
.fa-asterisk:before {
  content: "\f069";
}
.fa-exclamation-circle:before {
  content: "\f06a";
}
.fa-gift:before {
  content: "\f06b";
}
.fa-leaf:before {
  content: "\f06c";
}
.fa-fire:before {
  content: "\f06d";
}
.fa-eye:before {
  content: "\f06e";
}
.fa-eye-slash:before {
  content: "\f070";
}
.fa-warning:before,
.fa-exclamation-triangle:before {
  content: "\f071";
}
.fa-plane:before {
  content: "\f072";
}
.fa-calendar:before {
  content: "\f073";
}
.fa-random:before {
  content: "\f074";
}
.fa-comment:before {
  content: "\f075";
}
.fa-magnet:before {
  content: "\f076";
}
.fa-chevron-up:before {
  content: "\f077";
}
.fa-chevron-down:before {
  content: "\f078";
}
.fa-retweet:before {
  content: "\f079";
}
.fa-shopping-cart:before {
  content: "\f07a";
}
.fa-folder:before {
  content: "\f07b";
}
.fa-folder-open:before {
  content: "\f07c";
}
.fa-arrows-v:before {
  content: "\f07d";
}
.fa-arrows-h:before {
  content: "\f07e";
}
.fa-bar-chart-o:before,
.fa-bar-chart:before {
  content: "\f080";
}
.fa-twitter-square:before {
  content: "\f081";
}
.fa-facebook-square:before {
  content: "\f082";
}
.fa-camera-retro:before {
  content: "\f083";
}
.fa-key:before {
  content: "\f084";
}
.fa-gears:before,
.fa-cogs:before {
  content: "\f085";
}
.fa-comments:before {
  content: "\f086";
}
.fa-thumbs-o-up:before {
  content: "\f087";
}
.fa-thumbs-o-down:before {
  content: "\f088";
}
.fa-star-half:before {
  content: "\f089";
}
.fa-heart-o:before {
  content: "\f08a";
}
.fa-sign-out:before {
  content: "\f08b";
}
.fa-linkedin-square:before {
  content: "\f08c";
}
.fa-thumb-tack:before {
  content: "\f08d";
}
.fa-external-link:before {
  content: "\f08e";
}
.fa-sign-in:before {
  content: "\f090";
}
.fa-trophy:before {
  content: "\f091";
}
.fa-github-square:before {
  content: "\f092";
}
.fa-upload:before {
  content: "\f093";
}
.fa-lemon-o:before {
  content: "\f094";
}
.fa-phone:before {
  content: "\f095";
}
.fa-square-o:before {
  content: "\f096";
}
.fa-bookmark-o:before {
  content: "\f097";
}
.fa-phone-square:before {
  content: "\f098";
}
.fa-twitter:before {
  content: "\f099";
}
.fa-facebook:before {
  content: "\f09a";
}
.fa-github:before {
  content: "\f09b";
}
.fa-unlock:before {
  content: "\f09c";
}
.fa-credit-card:before {
  content: "\f09d";
}
.fa-rss:before {
  content: "\f09e";
}
.fa-hdd-o:before {
  content: "\f0a0";
}
.fa-bullhorn:before {
  content: "\f0a1";
}
.fa-bell:before {
  content: "\f0f3";
}
.fa-certificate:before {
  content: "\f0a3";
}
.fa-hand-o-right:before {
  content: "\f0a4";
}
.fa-hand-o-left:before {
  content: "\f0a5";
}
.fa-hand-o-up:before {
  content: "\f0a6";
}
.fa-hand-o-down:before {
  content: "\f0a7";
}
.fa-arrow-circle-left:before {
  content: "\f0a8";
}
.fa-arrow-circle-right:before {
  content: "\f0a9";
}
.fa-arrow-circle-up:before {
  content: "\f0aa";
}
.fa-arrow-circle-down:before {
  content: "\f0ab";
}
.fa-globe:before {
  content: "\f0ac";
}
.fa-wrench:before {
  content: "\f0ad";
}
.fa-tasks:before {
  content: "\f0ae";
}
.fa-filter:before {
  content: "\f0b0";
}
.fa-briefcase:before {
  content: "\f0b1";
}
.fa-arrows-alt:before {
  content: "\f0b2";
}
.fa-group:before,
.fa-users:before {
  content: "\f0c0";
}
.fa-chain:before,
.fa-link:before {
  content: "\f0c1";
}
.fa-cloud:before {
  content: "\f0c2";
}
.fa-flask:before {
  content: "\f0c3";
}
.fa-cut:before,
.fa-scissors:before {
  content: "\f0c4";
}
.fa-copy:before,
.fa-files-o:before {
  content: "\f0c5";
}
.fa-paperclip:before {
  content: "\f0c6";
}
.fa-save:before,
.fa-floppy-o:before {
  content: "\f0c7";
}
.fa-square:before {
  content: "\f0c8";
}
.fa-navicon:before,
.fa-reorder:before,
.fa-bars:before {
  content: "\f0c9";
}
.fa-list-ul:before {
  content: "\f0ca";
}
.fa-list-ol:before {
  content: "\f0cb";
}
.fa-strikethrough:before {
  content: "\f0cc";
}
.fa-underline:before {
  content: "\f0cd";
}
.fa-table:before {
  content: "\f0ce";
}
.fa-magic:before {
  content: "\f0d0";
}
.fa-truck:before {
  content: "\f0d1";
}
.fa-pinterest:before {
  content: "\f0d2";
}
.fa-pinterest-square:before {
  content: "\f0d3";
}
.fa-google-plus-square:before {
  content: "\f0d4";
}
.fa-google-plus:before {
  content: "\f0d5";
}
.fa-money:before {
  content: "\f0d6";
}
.fa-caret-down:before {
  content: "\f0d7";
}
.fa-caret-up:before {
  content: "\f0d8";
}
.fa-caret-left:before {
  content: "\f0d9";
}
.fa-caret-right:before {
  content: "\f0da";
}
.fa-columns:before {
  content: "\f0db";
}
.fa-unsorted:before,
.fa-sort:before {
  content: "\f0dc";
}
.fa-sort-down:before,
.fa-sort-desc:before {
  content: "\f0dd";
}
.fa-sort-up:before,
.fa-sort-asc:before {
  content: "\f0de";
}
.fa-envelope:before {
  content: "\f0e0";
}
.fa-linkedin:before {
  content: "\f0e1";
}
.fa-rotate-left:before,
.fa-undo:before {
  content: "\f0e2";
}
.fa-legal:before,
.fa-gavel:before {
  content: "\f0e3";
}
.fa-dashboard:before,
.fa-tachometer:before {
  content: "\f0e4";
}
.fa-comment-o:before {
  content: "\f0e5";
}
.fa-comments-o:before {
  content: "\f0e6";
}
.fa-flash:before,
.fa-bolt:before {
  content: "\f0e7";
}
.fa-sitemap:before {
  content: "\f0e8";
}
.fa-umbrella:before {
  content: "\f0e9";
}
.fa-paste:before,
.fa-clipboard:before {
  content: "\f0ea";
}
.fa-lightbulb-o:before {
  content: "\f0eb";
}
.fa-exchange:before {
  content: "\f0ec";
}
.fa-cloud-download:before {
  content: "\f0ed";
}
.fa-cloud-upload:before {
  content: "\f0ee";
}
.fa-user-md:before {
  content: "\f0f0";
}
.fa-stethoscope:before {
  content: "\f0f1";
}
.fa-suitcase:before {
  content: "\f0f2";
}
.fa-bell-o:before {
  content: "\f0a2";
}
.fa-coffee:before {
  content: "\f0f4";
}
.fa-cutlery:before {
  content: "\f0f5";
}
.fa-file-text-o:before {
  content: "\f0f6";
}
.fa-building-o:before {
  content: "\f0f7";
}
.fa-hospital-o:before {
  content: "\f0f8";
}
.fa-ambulance:before {
  content: "\f0f9";
}
.fa-medkit:before {
  content: "\f0fa";
}
.fa-fighter-jet:before {
  content: "\f0fb";
}
.fa-beer:before {
  content: "\f0fc";
}
.fa-h-square:before {
  content: "\f0fd";
}
.fa-plus-square:before {
  content: "\f0fe";
}
.fa-angle-double-left:before {
  content: "\f100";
}
.fa-angle-double-right:before {
  content: "\f101";
}
.fa-angle-double-up:before {
  content: "\f102";
}
.fa-angle-double-down:before {
  content: "\f103";
}
.fa-angle-left:before {
  content: "\f104";
}
.fa-angle-right:before {
  content: "\f105";
}
.fa-angle-up:before {
  content: "\f106";
}
.fa-angle-down:before {
  content: "\f107";
}
.fa-desktop:before {
  content: "\f108";
}
.fa-laptop:before {
  content: "\f109";
}
.fa-tablet:before {
  content: "\f10a";
}
.fa-mobile-phone:before,
.fa-mobile:before {
  content: "\f10b";
}
.fa-circle-o:before {
  content: "\f10c";
}
.fa-quote-left:before {
  content: "\f10d";
}
.fa-quote-right:before {
  content: "\f10e";
}
.fa-spinner:before {
  content: "\f110";
}
.fa-circle:before {
  content: "\f111";
}
.fa-mail-reply:before,
.fa-reply:before {
  content: "\f112";
}
.fa-github-alt:before {
  content: "\f113";
}
.fa-folder-o:before {
  content: "\f114";
}
.fa-folder-open-o:before {
  content: "\f115";
}
.fa-smile-o:before {
  content: "\f118";
}
.fa-frown-o:before {
  content: "\f119";
}
.fa-meh-o:before {
  content: "\f11a";
}
.fa-gamepad:before {
  content: "\f11b";
}
.fa-keyboard-o:before {
  content: "\f11c";
}
.fa-flag-o:before {
  content: "\f11d";
}
.fa-flag-checkered:before {
  content: "\f11e";
}
.fa-terminal:before {
  content: "\f120";
}
.fa-code:before {
  content: "\f121";
}
.fa-mail-reply-all:before,
.fa-reply-all:before {
  content: "\f122";
}
.fa-star-half-empty:before,
.fa-star-half-full:before,
.fa-star-half-o:before {
  content: "\f123";
}
.fa-location-arrow:before {
  content: "\f124";
}
.fa-crop:before {
  content: "\f125";
}
.fa-code-fork:before {
  content: "\f126";
}
.fa-unlink:before,
.fa-chain-broken:before {
  content: "\f127";
}
.fa-question:before {
  content: "\f128";
}
.fa-info:before {
  content: "\f129";
}
.fa-exclamation:before {
  content: "\f12a";
}
.fa-superscript:before {
  content: "\f12b";
}
.fa-subscript:before {
  content: "\f12c";
}
.fa-eraser:before {
  content: "\f12d";
}
.fa-puzzle-piece:before {
  content: "\f12e";
}
.fa-microphone:before {
  content: "\f130";
}
.fa-microphone-slash:before {
  content: "\f131";
}
.fa-shield:before {
  content: "\f132";
}
.fa-calendar-o:before {
  content: "\f133";
}
.fa-fire-extinguisher:before {
  content: "\f134";
}
.fa-rocket:before {
  content: "\f135";
}
.fa-maxcdn:before {
  content: "\f136";
}
.fa-chevron-circle-left:before {
  content: "\f137";
}
.fa-chevron-circle-right:before {
  content: "\f138";
}
.fa-chevron-circle-up:before {
  content: "\f139";
}
.fa-chevron-circle-down:before {
  content: "\f13a";
}
.fa-html5:before {
  content: "\f13b";
}
.fa-css3:before {
  content: "\f13c";
}
.fa-anchor:before {
  content: "\f13d";
}
.fa-unlock-alt:before {
  content: "\f13e";
}
.fa-bullseye:before {
  content: "\f140";
}
.fa-ellipsis-h:before {
  content: "\f141";
}
.fa-ellipsis-v:before {
  content: "\f142";
}
.fa-rss-square:before {
  content: "\f143";
}
.fa-play-circle:before {
  content: "\f144";
}
.fa-ticket:before {
  content: "\f145";
}
.fa-minus-square:before {
  content: "\f146";
}
.fa-minus-square-o:before {
  content: "\f147";
}
.fa-level-up:before {
  content: "\f148";
}
.fa-level-down:before {
  content: "\f149";
}
.fa-check-square:before {
  content: "\f14a";
}
.fa-pencil-square:before {
  content: "\f14b";
}
.fa-external-link-square:before {
  content: "\f14c";
}
.fa-share-square:before {
  content: "\f14d";
}
.fa-compass:before {
  content: "\f14e";
}
.fa-toggle-down:before,
.fa-caret-square-o-down:before {
  content: "\f150";
}
.fa-toggle-up:before,
.fa-caret-square-o-up:before {
  content: "\f151";
}
.fa-toggle-right:before,
.fa-caret-square-o-right:before {
  content: "\f152";
}
.fa-euro:before,
.fa-eur:before {
  content: "\f153";
}
.fa-gbp:before {
  content: "\f154";
}
.fa-dollar:before,
.fa-usd:before {
  content: "\f155";
}
.fa-rupee:before,
.fa-inr:before {
  content: "\f156";
}
.fa-cny:before,
.fa-rmb:before,
.fa-yen:before,
.fa-jpy:before {
  content: "\f157";
}
.fa-ruble:before,
.fa-rouble:before,
.fa-rub:before {
  content: "\f158";
}
.fa-won:before,
.fa-krw:before {
  content: "\f159";
}
.fa-bitcoin:before,
.fa-btc:before {
  content: "\f15a";
}
.fa-file:before {
  content: "\f15b";
}
.fa-file-text:before {
  content: "\f15c";
}
.fa-sort-alpha-asc:before {
  content: "\f15d";
}
.fa-sort-alpha-desc:before {
  content: "\f15e";
}
.fa-sort-amount-asc:before {
  content: "\f160";
}
.fa-sort-amount-desc:before {
  content: "\f161";
}
.fa-sort-numeric-asc:before {
  content: "\f162";
}
.fa-sort-numeric-desc:before {
  content: "\f163";
}
.fa-thumbs-up:before {
  content: "\f164";
}
.fa-thumbs-down:before {
  content: "\f165";
}
.fa-youtube-square:before {
  content: "\f166";
}
.fa-youtube:before {
  content: "\f167";
}
.fa-xing:before {
  content: "\f168";
}
.fa-xing-square:before {
  content: "\f169";
}
.fa-youtube-play:before {
  content: "\f16a";
}
.fa-dropbox:before {
  content: "\f16b";
}
.fa-stack-overflow:before {
  content: "\f16c";
}
.fa-instagram:before {
  content: "\f16d";
}
.fa-flickr:before {
  content: "\f16e";
}
.fa-adn:before {
  content: "\f170";
}
.fa-bitbucket:before {
  content: "\f171";
}
.fa-bitbucket-square:before {
  content: "\f172";
}
.fa-tumblr:before {
  content: "\f173";
}
.fa-tumblr-square:before {
  content: "\f174";
}
.fa-long-arrow-down:before {
  content: "\f175";
}
.fa-long-arrow-up:before {
  content: "\f176";
}
.fa-long-arrow-left:before {
  content: "\f177";
}
.fa-long-arrow-right:before {
  content: "\f178";
}
.fa-apple:before {
  content: "\f179";
}
.fa-windows:before {
  content: "\f17a";
}
.fa-android:before {
  content: "\f17b";
}
.fa-linux:before {
  content: "\f17c";
}
.fa-dribbble:before {
  content: "\f17d";
}
.fa-skype:before {
  content: "\f17e";
}
.fa-foursquare:before {
  content: "\f180";
}
.fa-trello:before {
  content: "\f181";
}
.fa-female:before {
  content: "\f182";
}
.fa-male:before {
  content: "\f183";
}
.fa-gittip:before {
  content: "\f184";
}
.fa-sun-o:before {
  content: "\f185";
}
.fa-moon-o:before {
  content: "\f186";
}
.fa-archive:before {
  content: "\f187";
}
.fa-bug:before {
  content: "\f188";
}
.fa-vk:before {
  content: "\f189";
}
.fa-weibo:before {
  content: "\f18a";
}
.fa-renren:before {
  content: "\f18b";
}
.fa-pagelines:before {
  content: "\f18c";
}
.fa-stack-exchange:before {
  content: "\f18d";
}
.fa-arrow-circle-o-right:before {
  content: "\f18e";
}
.fa-arrow-circle-o-left:before {
  content: "\f190";
}
.fa-toggle-left:before,
.fa-caret-square-o-left:before {
  content: "\f191";
}
.fa-dot-circle-o:before {
  content: "\f192";
}
.fa-wheelchair:before {
  content: "\f193";
}
.fa-vimeo-square:before {
  content: "\f194";
}
.fa-turkish-lira:before,
.fa-try:before {
  content: "\f195";
}
.fa-plus-square-o:before {
  content: "\f196";
}
.fa-space-shuttle:before {
  content: "\f197";
}
.fa-slack:before {
  content: "\f198";
}
.fa-envelope-square:before {
  content: "\f199";
}
.fa-wordpress:before {
  content: "\f19a";
}
.fa-openid:before {
  content: "\f19b";
}
.fa-institution:before,
.fa-bank:before,
.fa-university:before {
  content: "\f19c";
}
.fa-mortar-board:before,
.fa-graduation-cap:before {
  content: "\f19d";
}
.fa-yahoo:before {
  content: "\f19e";
}
.fa-google:before {
  content: "\f1a0";
}
.fa-reddit:before {
  content: "\f1a1";
}
.fa-reddit-square:before {
  content: "\f1a2";
}
.fa-stumbleupon-circle:before {
  content: "\f1a3";
}
.fa-stumbleupon:before {
  content: "\f1a4";
}
.fa-delicious:before {
  content: "\f1a5";
}
.fa-digg:before {
  content: "\f1a6";
}
.fa-pied-piper:before {
  content: "\f1a7";
}
.fa-pied-piper-alt:before {
  content: "\f1a8";
}
.fa-drupal:before {
  content: "\f1a9";
}
.fa-joomla:before {
  content: "\f1aa";
}
.fa-language:before {
  content: "\f1ab";
}
.fa-fax:before {
  content: "\f1ac";
}
.fa-building:before {
  content: "\f1ad";
}
.fa-child:before {
  content: "\f1ae";
}
.fa-paw:before {
  content: "\f1b0";
}
.fa-spoon:before {
  content: "\f1b1";
}
.fa-cube:before {
  content: "\f1b2";
}
.fa-cubes:before {
  content: "\f1b3";
}
.fa-behance:before {
  content: "\f1b4";
}
.fa-behance-square:before {
  content: "\f1b5";
}
.fa-steam:before {
  content: "\f1b6";
}
.fa-steam-square:before {
  content: "\f1b7";
}
.fa-recycle:before {
  content: "\f1b8";
}
.fa-automobile:before,
.fa-car:before {
  content: "\f1b9";
}
.fa-cab:before,
.fa-taxi:before {
  content: "\f1ba";
}
.fa-tree:before {
  content: "\f1bb";
}
.fa-spotify:before {
  content: "\f1bc";
}
.fa-deviantart:before {
  content: "\f1bd";
}
.fa-soundcloud:before {
  content: "\f1be";
}
.fa-database:before {
  content: "\f1c0";
}
.fa-file-pdf-o:before {
  content: "\f1c1";
}
.fa-file-word-o:before {
  content: "\f1c2";
}
.fa-file-excel-o:before {
  content: "\f1c3";
}
.fa-file-powerpoint-o:before {
  content: "\f1c4";
}
.fa-file-photo-o:before,
.fa-file-picture-o:before,
.fa-file-image-o:before {
  content: "\f1c5";
}
.fa-file-zip-o:before,
.fa-file-archive-o:before {
  content: "\f1c6";
}
.fa-file-sound-o:before,
.fa-file-audio-o:before {
  content: "\f1c7";
}
.fa-file-movie-o:before,
.fa-file-video-o:before {
  content: "\f1c8";
}
.fa-file-code-o:before {
  content: "\f1c9";
}
.fa-vine:before {
  content: "\f1ca";
}
.fa-codepen:before {
  content: "\f1cb";
}
.fa-jsfiddle:before {
  content: "\f1cc";
}
.fa-life-bouy:before,
.fa-life-buoy:before,
.fa-life-saver:before,
.fa-support:before,
.fa-life-ring:before {
  content: "\f1cd";
}
.fa-circle-o-notch:before {
  content: "\f1ce";
}
.fa-ra:before,
.fa-rebel:before {
  content: "\f1d0";
}
.fa-ge:before,
.fa-empire:before {
  content: "\f1d1";
}
.fa-git-square:before {
  content: "\f1d2";
}
.fa-git:before {
  content: "\f1d3";
}
.fa-hacker-news:before {
  content: "\f1d4";
}
.fa-tencent-weibo:before {
  content: "\f1d5";
}
.fa-qq:before {
  content: "\f1d6";
}
.fa-wechat:before,
.fa-weixin:before {
  content: "\f1d7";
}
.fa-send:before,
.fa-paper-plane:before {
  content: "\f1d8";
}
.fa-send-o:before,
.fa-paper-plane-o:before {
  content: "\f1d9";
}
.fa-history:before {
  content: "\f1da";
}
.fa-circle-thin:before {
  content: "\f1db";
}
.fa-header:before {
  content: "\f1dc";
}
.fa-paragraph:before {
  content: "\f1dd";
}
.fa-sliders:before {
  content: "\f1de";
}
.fa-share-alt:before {
  content: "\f1e0";
}
.fa-share-alt-square:before {
  content: "\f1e1";
}
.fa-bomb:before {
  content: "\f1e2";
}
.fa-soccer-ball-o:before,
.fa-futbol-o:before {
  content: "\f1e3";
}
.fa-tty:before {
  content: "\f1e4";
}
.fa-binoculars:before {
  content: "\f1e5";
}
.fa-plug:before {
  content: "\f1e6";
}
.fa-slideshare:before {
  content: "\f1e7";
}
.fa-twitch:before {
  content: "\f1e8";
}
.fa-yelp:before {
  content: "\f1e9";
}
.fa-newspaper-o:before {
  content: "\f1ea";
}
.fa-wifi:before {
  content: "\f1eb";
}
.fa-calculator:before {
  content: "\f1ec";
}
.fa-paypal:before {
  content: "\f1ed";
}
.fa-google-wallet:before {
  content: "\f1ee";
}
.fa-cc-visa:before {
  content: "\f1f0";
}
.fa-cc-mastercard:before {
  content: "\f1f1";
}
.fa-cc-discover:before {
  content: "\f1f2";
}
.fa-cc-amex:before {
  content: "\f1f3";
}
.fa-cc-paypal:before {
  content: "\f1f4";
}
.fa-cc-stripe:before {
  content: "\f1f5";
}
.fa-bell-slash:before {
  content: "\f1f6";
}
.fa-bell-slash-o:before {
  content: "\f1f7";
}
.fa-trash:before {
  content: "\f1f8";
}
.fa-copyright:before {
  content: "\f1f9";
}
.fa-at:before {
  content: "\f1fa";
}
.fa-eyedropper:before {
  content: "\f1fb";
}
.fa-paint-brush:before {
  content: "\f1fc";
}
.fa-birthday-cake:before {
  content: "\f1fd";
}
.fa-area-chart:before {
  content: "\f1fe";
}
.fa-pie-chart:before {
  content: "\f200";
}
.fa-line-chart:before {
  content: "\f201";
}
.fa-lastfm:before {
  content: "\f202";
}
.fa-lastfm-square:before {
  content: "\f203";
}
.fa-toggle-off:before {
  content: "\f204";
}
.fa-toggle-on:before {
  content: "\f205";
}
.fa-bicycle:before {
  content: "\f206";
}
.fa-bus:before {
  content: "\f207";
}
.fa-ioxhost:before {
  content: "\f208";
}
.fa-angellist:before {
  content: "\f209";
}
.fa-cc:before {
  content: "\f20a";
}
.fa-shekel:before,
.fa-sheqel:before,
.fa-ils:before {
  content: "\f20b";
}
.fa-meanpath:before {
  content: "\f20c";
}
/*!
*
* IPython base
*
*/
.modal.fade .modal-dialog {
  -webkit-transform: translate(0, 0);
  -ms-transform: translate(0, 0);
  -o-transform: translate(0, 0);
  transform: translate(0, 0);
}
code {
  color: #000;
}
pre {
  font-size: inherit;
  line-height: inherit;
}
label {
  font-weight: normal;
}
/* Make the page background atleast 100% the height of the view port */
/* Make the page itself atleast 70% the height of the view port */
.border-box-sizing {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
.corner-all {
  border-radius: 2px;
}
.no-padding {
  padding: 0px;
}
/* Flexible box model classes */
/* Taken from Alex Russell http://infrequently.org/2009/08/css-3-progress/ */
/* This file is a compatability layer.  It allows the usage of flexible box 
model layouts accross multiple browsers, including older browsers.  The newest,
universal implementation of the flexible box model is used when available (see
`Modern browsers` comments below).  Browsers that are known to implement this 
new spec completely include:

    Firefox 28.0+
    Chrome 29.0+
    Internet Explorer 11+ 
    Opera 17.0+

Browsers not listed, including Safari, are supported via the styling under the
`Old browsers` comments below.
*/
.hbox {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
.hbox > * {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
}
.vbox {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
.vbox > * {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
}
.hbox.reverse,
.vbox.reverse,
.reverse {
  /* Old browsers */
  -webkit-box-direction: reverse;
  -moz-box-direction: reverse;
  box-direction: reverse;
  /* Modern browsers */
  flex-direction: row-reverse;
}
.hbox.box-flex0,
.vbox.box-flex0,
.box-flex0 {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
  width: auto;
}
.hbox.box-flex1,
.vbox.box-flex1,
.box-flex1 {
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
.hbox.box-flex,
.vbox.box-flex,
.box-flex {
  /* Old browsers */
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
.hbox.box-flex2,
.vbox.box-flex2,
.box-flex2 {
  /* Old browsers */
  -webkit-box-flex: 2;
  -moz-box-flex: 2;
  box-flex: 2;
  /* Modern browsers */
  flex: 2;
}
.box-group1 {
  /*  Deprecated */
  -webkit-box-flex-group: 1;
  -moz-box-flex-group: 1;
  box-flex-group: 1;
}
.box-group2 {
  /* Deprecated */
  -webkit-box-flex-group: 2;
  -moz-box-flex-group: 2;
  box-flex-group: 2;
}
.hbox.start,
.vbox.start,
.start {
  /* Old browsers */
  -webkit-box-pack: start;
  -moz-box-pack: start;
  box-pack: start;
  /* Modern browsers */
  justify-content: flex-start;
}
.hbox.end,
.vbox.end,
.end {
  /* Old browsers */
  -webkit-box-pack: end;
  -moz-box-pack: end;
  box-pack: end;
  /* Modern browsers */
  justify-content: flex-end;
}
.hbox.center,
.vbox.center,
.center {
  /* Old browsers */
  -webkit-box-pack: center;
  -moz-box-pack: center;
  box-pack: center;
  /* Modern browsers */
  justify-content: center;
}
.hbox.baseline,
.vbox.baseline,
.baseline {
  /* Old browsers */
  -webkit-box-pack: baseline;
  -moz-box-pack: baseline;
  box-pack: baseline;
  /* Modern browsers */
  justify-content: baseline;
}
.hbox.stretch,
.vbox.stretch,
.stretch {
  /* Old browsers */
  -webkit-box-pack: stretch;
  -moz-box-pack: stretch;
  box-pack: stretch;
  /* Modern browsers */
  justify-content: stretch;
}
.hbox.align-start,
.vbox.align-start,
.align-start {
  /* Old browsers */
  -webkit-box-align: start;
  -moz-box-align: start;
  box-align: start;
  /* Modern browsers */
  align-items: flex-start;
}
.hbox.align-end,
.vbox.align-end,
.align-end {
  /* Old browsers */
  -webkit-box-align: end;
  -moz-box-align: end;
  box-align: end;
  /* Modern browsers */
  align-items: flex-end;
}
.hbox.align-center,
.vbox.align-center,
.align-center {
  /* Old browsers */
  -webkit-box-align: center;
  -moz-box-align: center;
  box-align: center;
  /* Modern browsers */
  align-items: center;
}
.hbox.align-baseline,
.vbox.align-baseline,
.align-baseline {
  /* Old browsers */
  -webkit-box-align: baseline;
  -moz-box-align: baseline;
  box-align: baseline;
  /* Modern browsers */
  align-items: baseline;
}
.hbox.align-stretch,
.vbox.align-stretch,
.align-stretch {
  /* Old browsers */
  -webkit-box-align: stretch;
  -moz-box-align: stretch;
  box-align: stretch;
  /* Modern browsers */
  align-items: stretch;
}
div.error {
  margin: 2em;
  text-align: center;
}
div.error > h1 {
  font-size: 500%;
  line-height: normal;
}
div.error > p {
  font-size: 200%;
  line-height: normal;
}
div.traceback-wrapper {
  text-align: left;
  max-width: 800px;
  margin: auto;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
body {
  background-color: #fff;
  /* This makes sure that the body covers the entire window and needs to
       be in a different element than the display: box in wrapper below */
  position: absolute;
  left: 0px;
  right: 0px;
  top: 0px;
  bottom: 0px;
  overflow: visible;
}
body > #header {
  /* Initially hidden to prevent FLOUC */
  display: none;
  background-color: #fff;
  /* Display over codemirror */
  position: relative;
  z-index: 100;
}
body > #header #header-container {
  padding-bottom: 5px;
  padding-top: 5px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
body > #header .header-bar {
  width: 100%;
  height: 1px;
  background: #e7e7e7;
  margin-bottom: -1px;
}
@media print {
  body > #header {
    display: none !important;
  }
}
#header-spacer {
  width: 100%;
  visibility: hidden;
}
@media print {
  #header-spacer {
    display: none;
  }
}
#ipython_notebook {
  padding-left: 0px;
  padding-top: 1px;
  padding-bottom: 1px;
}
@media (max-width: 991px) {
  #ipython_notebook {
    margin-left: 10px;
  }
}
[dir="rtl"] #ipython_notebook {
  float: right !important;
}
#noscript {
  width: auto;
  padding-top: 16px;
  padding-bottom: 16px;
  text-align: center;
  font-size: 22px;
  color: red;
  font-weight: bold;
}
#ipython_notebook img {
  height: 28px;
}
#site {
  width: 100%;
  display: none;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  overflow: auto;
}
@media print {
  #site {
    height: auto !important;
  }
}
/* Smaller buttons */
.ui-button .ui-button-text {
  padding: 0.2em 0.8em;
  font-size: 77%;
}
input.ui-button {
  padding: 0.3em 0.9em;
}
span#login_widget {
  float: right;
}
span#login_widget > .button,
#logout {
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
span#login_widget > .button:focus,
#logout:focus,
span#login_widget > .button.focus,
#logout.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
span#login_widget > .button:hover,
#logout:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
span#login_widget > .button:active,
#logout:active,
span#login_widget > .button.active,
#logout.active,
.open > .dropdown-togglespan#login_widget > .button,
.open > .dropdown-toggle#logout {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
span#login_widget > .button:active:hover,
#logout:active:hover,
span#login_widget > .button.active:hover,
#logout.active:hover,
.open > .dropdown-togglespan#login_widget > .button:hover,
.open > .dropdown-toggle#logout:hover,
span#login_widget > .button:active:focus,
#logout:active:focus,
span#login_widget > .button.active:focus,
#logout.active:focus,
.open > .dropdown-togglespan#login_widget > .button:focus,
.open > .dropdown-toggle#logout:focus,
span#login_widget > .button:active.focus,
#logout:active.focus,
span#login_widget > .button.active.focus,
#logout.active.focus,
.open > .dropdown-togglespan#login_widget > .button.focus,
.open > .dropdown-toggle#logout.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
span#login_widget > .button:active,
#logout:active,
span#login_widget > .button.active,
#logout.active,
.open > .dropdown-togglespan#login_widget > .button,
.open > .dropdown-toggle#logout {
  background-image: none;
}
span#login_widget > .button.disabled:hover,
#logout.disabled:hover,
span#login_widget > .button[disabled]:hover,
#logout[disabled]:hover,
fieldset[disabled] span#login_widget > .button:hover,
fieldset[disabled] #logout:hover,
span#login_widget > .button.disabled:focus,
#logout.disabled:focus,
span#login_widget > .button[disabled]:focus,
#logout[disabled]:focus,
fieldset[disabled] span#login_widget > .button:focus,
fieldset[disabled] #logout:focus,
span#login_widget > .button.disabled.focus,
#logout.disabled.focus,
span#login_widget > .button[disabled].focus,
#logout[disabled].focus,
fieldset[disabled] span#login_widget > .button.focus,
fieldset[disabled] #logout.focus {
  background-color: #fff;
  border-color: #ccc;
}
span#login_widget > .button .badge,
#logout .badge {
  color: #fff;
  background-color: #333;
}
.nav-header {
  text-transform: none;
}
#header > span {
  margin-top: 10px;
}
.modal_stretch .modal-dialog {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  min-height: 80vh;
}
.modal_stretch .modal-dialog .modal-body {
  max-height: calc(100vh - 200px);
  overflow: auto;
  flex: 1;
}
@media (min-width: 768px) {
  .modal .modal-dialog {
    width: 700px;
  }
}
@media (min-width: 768px) {
  select.form-control {
    margin-left: 12px;
    margin-right: 12px;
  }
}
/*!
*
* IPython auth
*
*/
.center-nav {
  display: inline-block;
  margin-bottom: -4px;
}
/*!
*
* IPython tree view
*
*/
/* We need an invisible input field on top of the sentense*/
/* "Drag file onto the list ..." */
.alternate_upload {
  background-color: none;
  display: inline;
}
.alternate_upload.form {
  padding: 0;
  margin: 0;
}
.alternate_upload input.fileinput {
  text-align: center;
  vertical-align: middle;
  display: inline;
  opacity: 0;
  z-index: 2;
  width: 12ex;
  margin-right: -12ex;
}
.alternate_upload .btn-upload {
  height: 22px;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
[dir="rtl"] #tabs li {
  float: right;
}
ul#tabs {
  margin-bottom: 4px;
}
[dir="rtl"] ul#tabs {
  margin-right: 0px;
}
ul#tabs a {
  padding-top: 6px;
  padding-bottom: 4px;
}
ul.breadcrumb a:focus,
ul.breadcrumb a:hover {
  text-decoration: none;
}
ul.breadcrumb i.icon-home {
  font-size: 16px;
  margin-right: 4px;
}
ul.breadcrumb span {
  color: #5e5e5e;
}
.list_toolbar {
  padding: 4px 0 4px 0;
  vertical-align: middle;
}
.list_toolbar .tree-buttons {
  padding-top: 1px;
}
[dir="rtl"] .list_toolbar .tree-buttons {
  float: left !important;
}
[dir="rtl"] .list_toolbar .pull-right {
  padding-top: 1px;
  float: left !important;
}
[dir="rtl"] .list_toolbar .pull-left {
  float: right !important;
}
.dynamic-buttons {
  padding-top: 3px;
  display: inline-block;
}
.list_toolbar [class*="span"] {
  min-height: 24px;
}
.list_header {
  font-weight: bold;
  background-color: #EEE;
}
.list_placeholder {
  font-weight: bold;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
}
.list_container {
  margin-top: 4px;
  margin-bottom: 20px;
  border: 1px solid #ddd;
  border-radius: 2px;
}
.list_container > div {
  border-bottom: 1px solid #ddd;
}
.list_container > div:hover .list-item {
  background-color: red;
}
.list_container > div:last-child {
  border: none;
}
.list_item:hover .list_item {
  background-color: #ddd;
}
.list_item a {
  text-decoration: none;
}
.list_item:hover {
  background-color: #fafafa;
}
.list_header > div,
.list_item > div {
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
  line-height: 22px;
}
.list_header > div input,
.list_item > div input {
  margin-right: 7px;
  margin-left: 14px;
  vertical-align: baseline;
  line-height: 22px;
  position: relative;
  top: -1px;
}
.list_header > div .item_link,
.list_item > div .item_link {
  margin-left: -1px;
  vertical-align: baseline;
  line-height: 22px;
}
.new-file input[type=checkbox] {
  visibility: hidden;
}
.item_name {
  line-height: 22px;
  height: 24px;
}
.item_icon {
  font-size: 14px;
  color: #5e5e5e;
  margin-right: 7px;
  margin-left: 7px;
  line-height: 22px;
  vertical-align: baseline;
}
.item_buttons {
  line-height: 1em;
  margin-left: -5px;
}
.item_buttons .btn,
.item_buttons .btn-group,
.item_buttons .input-group {
  float: left;
}
.item_buttons > .btn,
.item_buttons > .btn-group,
.item_buttons > .input-group {
  margin-left: 5px;
}
.item_buttons .btn {
  min-width: 13ex;
}
.item_buttons .running-indicator {
  padding-top: 4px;
  color: #5cb85c;
}
.item_buttons .kernel-name {
  padding-top: 4px;
  color: #5bc0de;
  margin-right: 7px;
  float: left;
}
.toolbar_info {
  height: 24px;
  line-height: 24px;
}
.list_item input:not([type=checkbox]) {
  padding-top: 3px;
  padding-bottom: 3px;
  height: 22px;
  line-height: 14px;
  margin: 0px;
}
.highlight_text {
  color: blue;
}
#project_name {
  display: inline-block;
  padding-left: 7px;
  margin-left: -2px;
}
#project_name > .breadcrumb {
  padding: 0px;
  margin-bottom: 0px;
  background-color: transparent;
  font-weight: bold;
}
#tree-selector {
  padding-right: 0px;
}
[dir="rtl"] #tree-selector a {
  float: right;
}
#button-select-all {
  min-width: 50px;
}
#select-all {
  margin-left: 7px;
  margin-right: 2px;
}
.menu_icon {
  margin-right: 2px;
}
.tab-content .row {
  margin-left: 0px;
  margin-right: 0px;
}
.folder_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f114";
}
.folder_icon:before.pull-left {
  margin-right: .3em;
}
.folder_icon:before.pull-right {
  margin-left: .3em;
}
.notebook_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f02d";
  position: relative;
  top: -1px;
}
.notebook_icon:before.pull-left {
  margin-right: .3em;
}
.notebook_icon:before.pull-right {
  margin-left: .3em;
}
.running_notebook_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f02d";
  position: relative;
  top: -1px;
  color: #5cb85c;
}
.running_notebook_icon:before.pull-left {
  margin-right: .3em;
}
.running_notebook_icon:before.pull-right {
  margin-left: .3em;
}
.file_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f016";
  position: relative;
  top: -2px;
}
.file_icon:before.pull-left {
  margin-right: .3em;
}
.file_icon:before.pull-right {
  margin-left: .3em;
}
#notebook_toolbar .pull-right {
  padding-top: 0px;
  margin-right: -1px;
}
ul#new-menu {
  left: auto;
  right: 0;
}
[dir="rtl"] #new-menu {
  text-align: right;
}
.kernel-menu-icon {
  padding-right: 12px;
  width: 24px;
  content: "\f096";
}
.kernel-menu-icon:before {
  content: "\f096";
}
.kernel-menu-icon-current:before {
  content: "\f00c";
}
#tab_content {
  padding-top: 20px;
}
#running .panel-group .panel {
  margin-top: 3px;
  margin-bottom: 1em;
}
#running .panel-group .panel .panel-heading {
  background-color: #EEE;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
  line-height: 22px;
}
#running .panel-group .panel .panel-heading a:focus,
#running .panel-group .panel .panel-heading a:hover {
  text-decoration: none;
}
#running .panel-group .panel .panel-body {
  padding: 0px;
}
#running .panel-group .panel .panel-body .list_container {
  margin-top: 0px;
  margin-bottom: 0px;
  border: 0px;
  border-radius: 0px;
}
#running .panel-group .panel .panel-body .list_container .list_item {
  border-bottom: 1px solid #ddd;
}
#running .panel-group .panel .panel-body .list_container .list_item:last-child {
  border-bottom: 0px;
}
[dir="rtl"] #running .col-sm-8 {
  float: right !important;
}
.delete-button {
  display: none;
}
.duplicate-button {
  display: none;
}
.rename-button {
  display: none;
}
.shutdown-button {
  display: none;
}
.dynamic-instructions {
  display: inline-block;
  padding-top: 4px;
}
/*!
*
* IPython text editor webapp
*
*/
.selected-keymap i.fa {
  padding: 0px 5px;
}
.selected-keymap i.fa:before {
  content: "\f00c";
}
#mode-menu {
  overflow: auto;
  max-height: 20em;
}
.edit_app #header {
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
.edit_app #menubar .navbar {
  /* Use a negative 1 bottom margin, so the border overlaps the border of the
    header */
  margin-bottom: -1px;
}
.dirty-indicator {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator.pull-left {
  margin-right: .3em;
}
.dirty-indicator.pull-right {
  margin-left: .3em;
}
.dirty-indicator-dirty {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator-dirty.pull-left {
  margin-right: .3em;
}
.dirty-indicator-dirty.pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator-clean.pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean.pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f00c";
}
.dirty-indicator-clean:before.pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean:before.pull-right {
  margin-left: .3em;
}
#filename {
  font-size: 16pt;
  display: table;
  padding: 0px 5px;
}
#current-mode {
  padding-left: 5px;
  padding-right: 5px;
}
#texteditor-backdrop {
  padding-top: 20px;
  padding-bottom: 20px;
}
@media not print {
  #texteditor-backdrop {
    background-color: #EEE;
  }
}
@media print {
  #texteditor-backdrop #texteditor-container .CodeMirror-gutter,
  #texteditor-backdrop #texteditor-container .CodeMirror-gutters {
    background-color: #fff;
  }
}
@media not print {
  #texteditor-backdrop #texteditor-container .CodeMirror-gutter,
  #texteditor-backdrop #texteditor-container .CodeMirror-gutters {
    background-color: #fff;
  }
}
@media not print {
  #texteditor-backdrop #texteditor-container {
    padding: 0px;
    background-color: #fff;
    -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
    box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  }
}
/*!
*
* IPython notebook
*
*/
/* CSS font colors for translated ANSI colors. */
.ansibold {
  font-weight: bold;
}
/* use dark versions for foreground, to improve visibility */
.ansiblack {
  color: black;
}
.ansired {
  color: darkred;
}
.ansigreen {
  color: darkgreen;
}
.ansiyellow {
  color: #c4a000;
}
.ansiblue {
  color: darkblue;
}
.ansipurple {
  color: darkviolet;
}
.ansicyan {
  color: steelblue;
}
.ansigray {
  color: gray;
}
/* and light for background, for the same reason */
.ansibgblack {
  background-color: black;
}
.ansibgred {
  background-color: red;
}
.ansibggreen {
  background-color: green;
}
.ansibgyellow {
  background-color: yellow;
}
.ansibgblue {
  background-color: blue;
}
.ansibgpurple {
  background-color: magenta;
}
.ansibgcyan {
  background-color: cyan;
}
.ansibggray {
  background-color: gray;
}
div.cell {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  border-radius: 2px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  border-width: 1px;
  border-style: solid;
  border-color: transparent;
  width: 100%;
  padding: 5px;
  /* This acts as a spacer between cells, that is outside the border */
  margin: 0px;
  outline: none;
  border-left-width: 1px;
  padding-left: 5px;
  background: linear-gradient(to right, transparent -40px, transparent 1px, transparent 1px, transparent 100%);
}
div.cell.jupyter-soft-selected {
  border-left-color: #90CAF9;
  border-left-color: #E3F2FD;
  border-left-width: 1px;
  padding-left: 5px;
  border-right-color: #E3F2FD;
  border-right-width: 1px;
  background: #E3F2FD;
}
@media print {
  div.cell.jupyter-soft-selected {
    border-color: transparent;
  }
}
div.cell.selected {
  border-color: #ababab;
  border-left-width: 0px;
  padding-left: 6px;
  background: linear-gradient(to right, #42A5F5 -40px, #42A5F5 5px, transparent 5px, transparent 100%);
}
@media print {
  div.cell.selected {
    border-color: transparent;
  }
}
div.cell.selected.jupyter-soft-selected {
  border-left-width: 0;
  padding-left: 6px;
  background: linear-gradient(to right, #42A5F5 -40px, #42A5F5 7px, #E3F2FD 7px, #E3F2FD 100%);
}
.edit_mode div.cell.selected {
  border-color: #66BB6A;
  border-left-width: 0px;
  padding-left: 6px;
  background: linear-gradient(to right, #66BB6A -40px, #66BB6A 5px, transparent 5px, transparent 100%);
}
@media print {
  .edit_mode div.cell.selected {
    border-color: transparent;
  }
}
.prompt {
  /* This needs to be wide enough for 3 digit prompt numbers: In[100]: */
  min-width: 14ex;
  /* This padding is tuned to match the padding on the CodeMirror editor. */
  padding: 0.4em;
  margin: 0px;
  font-family: monospace;
  text-align: right;
  /* This has to match that of the the CodeMirror class line-height below */
  line-height: 1.21429em;
  /* Don't highlight prompt number selection */
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  /* Use default cursor */
  cursor: default;
}
@media (max-width: 540px) {
  .prompt {
    text-align: left;
  }
}
div.inner_cell {
  min-width: 0;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
/* input_area and input_prompt must match in top border and margin for alignment */
div.input_area {
  border: 1px solid #cfcfcf;
  border-radius: 2px;
  background: #f7f7f7;
  line-height: 1.21429em;
}
/* This is needed so that empty prompt areas can collapse to zero height when there
   is no content in the output_subarea and the prompt. The main purpose of this is
   to make sure that empty JavaScript output_subareas have no height. */
div.prompt:empty {
  padding-top: 0;
  padding-bottom: 0;
}
div.unrecognized_cell {
  padding: 5px 5px 5px 0px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
div.unrecognized_cell .inner_cell {
  border-radius: 2px;
  padding: 5px;
  font-weight: bold;
  color: red;
  border: 1px solid #cfcfcf;
  background: #eaeaea;
}
div.unrecognized_cell .inner_cell a {
  color: inherit;
  text-decoration: none;
}
div.unrecognized_cell .inner_cell a:hover {
  color: inherit;
  text-decoration: none;
}
@media (max-width: 540px) {
  div.unrecognized_cell > div.prompt {
    display: none;
  }
}
div.code_cell {
  /* avoid page breaking on code cells when printing */
}
@media print {
  div.code_cell {
    page-break-inside: avoid;
  }
}
/* any special styling for code cells that are currently running goes here */
div.input {
  page-break-inside: avoid;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.input {
    /* Old browsers */
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-box-align: stretch;
    display: -moz-box;
    -moz-box-orient: vertical;
    -moz-box-align: stretch;
    display: box;
    box-orient: vertical;
    box-align: stretch;
    /* Modern browsers */
    display: flex;
    flex-direction: column;
    align-items: stretch;
  }
}
/* input_area and input_prompt must match in top border and margin for alignment */
div.input_prompt {
  color: #303F9F;
  border-top: 1px solid transparent;
}
div.input_area > div.highlight {
  margin: 0.4em;
  border: none;
  padding: 0px;
  background-color: transparent;
}
div.input_area > div.highlight > pre {
  margin: 0px;
  border: none;
  padding: 0px;
  background-color: transparent;
}
/* The following gets added to the <head> if it is detected that the user has a
 * monospace font with inconsistent normal/bold/italic height.  See
 * notebookmain.js.  Such fonts will have keywords vertically offset with
 * respect to the rest of the text.  The user should select a better font.
 * See: https://github.com/ipython/ipython/issues/1503
 *
 * .CodeMirror span {
 *      vertical-align: bottom;
 * }
 */
.CodeMirror {
  line-height: 1.21429em;
  /* Changed from 1em to our global default */
  font-size: 14px;
  height: auto;
  /* Changed to auto to autogrow */
  background: none;
  /* Changed from white to allow our bg to show through */
}
.CodeMirror-scroll {
  /*  The CodeMirror docs are a bit fuzzy on if overflow-y should be hidden or visible.*/
  /*  We have found that if it is visible, vertical scrollbars appear with font size changes.*/
  overflow-y: hidden;
  overflow-x: auto;
}
.CodeMirror-lines {
  /* In CM2, this used to be 0.4em, but in CM3 it went to 4px. We need the em value because */
  /* we have set a different line-height and want this to scale with that. */
  padding: 0.4em;
}
.CodeMirror-linenumber {
  padding: 0 8px 0 4px;
}
.CodeMirror-gutters {
  border-bottom-left-radius: 2px;
  border-top-left-radius: 2px;
}
.CodeMirror pre {
  /* In CM3 this went to 4px from 0 in CM2. We need the 0 value because of how we size */
  /* .CodeMirror-lines */
  padding: 0;
  border: 0;
  border-radius: 0;
}
/*

Original style from softwaremaniacs.org (c) Ivan Sagalaev <Maniac@SoftwareManiacs.Org>
Adapted from GitHub theme

*/
.highlight-base {
  color: #000;
}
.highlight-variable {
  color: #000;
}
.highlight-variable-2 {
  color: #1a1a1a;
}
.highlight-variable-3 {
  color: #333333;
}
.highlight-string {
  color: #BA2121;
}
.highlight-comment {
  color: #408080;
  font-style: italic;
}
.highlight-number {
  color: #080;
}
.highlight-atom {
  color: #88F;
}
.highlight-keyword {
  color: #008000;
  font-weight: bold;
}
.highlight-builtin {
  color: #008000;
}
.highlight-error {
  color: #f00;
}
.highlight-operator {
  color: #AA22FF;
  font-weight: bold;
}
.highlight-meta {
  color: #AA22FF;
}
/* previously not defined, copying from default codemirror */
.highlight-def {
  color: #00f;
}
.highlight-string-2 {
  color: #f50;
}
.highlight-qualifier {
  color: #555;
}
.highlight-bracket {
  color: #997;
}
.highlight-tag {
  color: #170;
}
.highlight-attribute {
  color: #00c;
}
.highlight-header {
  color: blue;
}
.highlight-quote {
  color: #090;
}
.highlight-link {
  color: #00c;
}
/* apply the same style to codemirror */
.cm-s-ipython span.cm-keyword {
  color: #008000;
  font-weight: bold;
}
.cm-s-ipython span.cm-atom {
  color: #88F;
}
.cm-s-ipython span.cm-number {
  color: #080;
}
.cm-s-ipython span.cm-def {
  color: #00f;
}
.cm-s-ipython span.cm-variable {
  color: #000;
}
.cm-s-ipython span.cm-operator {
  color: #AA22FF;
  font-weight: bold;
}
.cm-s-ipython span.cm-variable-2 {
  color: #1a1a1a;
}
.cm-s-ipython span.cm-variable-3 {
  color: #333333;
}
.cm-s-ipython span.cm-comment {
  color: #408080;
  font-style: italic;
}
.cm-s-ipython span.cm-string {
  color: #BA2121;
}
.cm-s-ipython span.cm-string-2 {
  color: #f50;
}
.cm-s-ipython span.cm-meta {
  color: #AA22FF;
}
.cm-s-ipython span.cm-qualifier {
  color: #555;
}
.cm-s-ipython span.cm-builtin {
  color: #008000;
}
.cm-s-ipython span.cm-bracket {
  color: #997;
}
.cm-s-ipython span.cm-tag {
  color: #170;
}
.cm-s-ipython span.cm-attribute {
  color: #00c;
}
.cm-s-ipython span.cm-header {
  color: blue;
}
.cm-s-ipython span.cm-quote {
  color: #090;
}
.cm-s-ipython span.cm-link {
  color: #00c;
}
.cm-s-ipython span.cm-error {
  color: #f00;
}
.cm-s-ipython span.cm-tab {
  background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAMCAYAAAAkuj5RAAAAAXNSR0IArs4c6QAAAGFJREFUSMft1LsRQFAQheHPowAKoACx3IgEKtaEHujDjORSgWTH/ZOdnZOcM/sgk/kFFWY0qV8foQwS4MKBCS3qR6ixBJvElOobYAtivseIE120FaowJPN75GMu8j/LfMwNjh4HUpwg4LUAAAAASUVORK5CYII=);
  background-position: right;
  background-repeat: no-repeat;
}
div.output_wrapper {
  /* this position must be relative to enable descendents to be absolute within it */
  position: relative;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  z-index: 1;
}
/* class for the output area when it should be height-limited */
div.output_scroll {
  /* ideally, this would be max-height, but FF barfs all over that */
  height: 24em;
  /* FF needs this *and the wrapper* to specify full width, or it will shrinkwrap */
  width: 100%;
  overflow: auto;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.8);
  box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.8);
  display: block;
}
/* output div while it is collapsed */
div.output_collapsed {
  margin: 0px;
  padding: 0px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
div.out_prompt_overlay {
  height: 100%;
  padding: 0px 0.4em;
  position: absolute;
  border-radius: 2px;
}
div.out_prompt_overlay:hover {
  /* use inner shadow to get border that is computed the same on WebKit/FF */
  -webkit-box-shadow: inset 0 0 1px #000;
  box-shadow: inset 0 0 1px #000;
  background: rgba(240, 240, 240, 0.5);
}
div.output_prompt {
  color: #D84315;
}
/* This class is the outer container of all output sections. */
div.output_area {
  padding: 0px;
  page-break-inside: avoid;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
div.output_area .MathJax_Display {
  text-align: left !important;
}
div.output_area .rendered_html table {
  margin-left: 0;
  margin-right: 0;
}
div.output_area .rendered_html img {
  margin-left: 0;
  margin-right: 0;
}
div.output_area img,
div.output_area svg {
  max-width: 100%;
  height: auto;
}
div.output_area img.unconfined,
div.output_area svg.unconfined {
  max-width: none;
}
/* This is needed to protect the pre formating from global settings such
   as that of bootstrap */
.output {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.output_area {
    /* Old browsers */
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-box-align: stretch;
    display: -moz-box;
    -moz-box-orient: vertical;
    -moz-box-align: stretch;
    display: box;
    box-orient: vertical;
    box-align: stretch;
    /* Modern browsers */
    display: flex;
    flex-direction: column;
    align-items: stretch;
  }
}
div.output_area pre {
  margin: 0;
  padding: 0;
  border: 0;
  vertical-align: baseline;
  color: black;
  background-color: transparent;
  border-radius: 0;
}
/* This class is for the output subarea inside the output_area and after
   the prompt div. */
div.output_subarea {
  overflow-x: auto;
  padding: 0.4em;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
  max-width: calc(100% - 14ex);
}
div.output_scroll div.output_subarea {
  overflow-x: visible;
}
/* The rest of the output_* classes are for special styling of the different
   output types */
/* all text output has this class: */
div.output_text {
  text-align: left;
  color: #000;
  /* This has to match that of the the CodeMirror class line-height below */
  line-height: 1.21429em;
}
/* stdout/stderr are 'text' as well as 'stream', but execute_result/error are *not* streams */
div.output_stderr {
  background: #fdd;
  /* very light red background for stderr */
}
div.output_latex {
  text-align: left;
}
/* Empty output_javascript divs should have no height */
div.output_javascript:empty {
  padding: 0;
}
.js-error {
  color: darkred;
}
/* raw_input styles */
div.raw_input_container {
  line-height: 1.21429em;
  padding-top: 5px;
}
pre.raw_input_prompt {
  /* nothing needed here. */
}
input.raw_input {
  font-family: monospace;
  font-size: inherit;
  color: inherit;
  width: auto;
  /* make sure input baseline aligns with prompt */
  vertical-align: baseline;
  /* padding + margin = 0.5em between prompt and cursor */
  padding: 0em 0.25em;
  margin: 0em 0.25em;
}
input.raw_input:focus {
  box-shadow: none;
}
p.p-space {
  margin-bottom: 10px;
}
div.output_unrecognized {
  padding: 5px;
  font-weight: bold;
  color: red;
}
div.output_unrecognized a {
  color: inherit;
  text-decoration: none;
}
div.output_unrecognized a:hover {
  color: inherit;
  text-decoration: none;
}
.rendered_html {
  color: #000;
  /* any extras will just be numbers: */
}
.rendered_html em {
  font-style: italic;
}
.rendered_html strong {
  font-weight: bold;
}
.rendered_html u {
  text-decoration: underline;
}
.rendered_html :link {
  text-decoration: underline;
}
.rendered_html :visited {
  text-decoration: underline;
}
.rendered_html h1 {
  font-size: 185.7%;
  margin: 1.08em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h2 {
  font-size: 157.1%;
  margin: 1.27em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h3 {
  font-size: 128.6%;
  margin: 1.55em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h4 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h5 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
  font-style: italic;
}
.rendered_html h6 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
  font-style: italic;
}
.rendered_html h1:first-child {
  margin-top: 0.538em;
}
.rendered_html h2:first-child {
  margin-top: 0.636em;
}
.rendered_html h3:first-child {
  margin-top: 0.777em;
}
.rendered_html h4:first-child {
  margin-top: 1em;
}
.rendered_html h5:first-child {
  margin-top: 1em;
}
.rendered_html h6:first-child {
  margin-top: 1em;
}
.rendered_html ul {
  list-style: disc;
  margin: 0em 2em;
  padding-left: 0px;
}
.rendered_html ul ul {
  list-style: square;
  margin: 0em 2em;
}
.rendered_html ul ul ul {
  list-style: circle;
  margin: 0em 2em;
}
.rendered_html ol {
  list-style: decimal;
  margin: 0em 2em;
  padding-left: 0px;
}
.rendered_html ol ol {
  list-style: upper-alpha;
  margin: 0em 2em;
}
.rendered_html ol ol ol {
  list-style: lower-alpha;
  margin: 0em 2em;
}
.rendered_html ol ol ol ol {
  list-style: lower-roman;
  margin: 0em 2em;
}
.rendered_html ol ol ol ol ol {
  list-style: decimal;
  margin: 0em 2em;
}
.rendered_html * + ul {
  margin-top: 1em;
}
.rendered_html * + ol {
  margin-top: 1em;
}
.rendered_html hr {
  color: black;
  background-color: black;
}
.rendered_html pre {
  margin: 1em 2em;
}
.rendered_html pre,
.rendered_html code {
  border: 0;
  background-color: #fff;
  color: #000;
  font-size: 100%;
  padding: 0px;
}
.rendered_html blockquote {
  margin: 1em 2em;
}
.rendered_html table {
  margin-left: auto;
  margin-right: auto;
  border: 1px solid black;
  border-collapse: collapse;
}
.rendered_html tr,
.rendered_html th,
.rendered_html td {
  border: 1px solid black;
  border-collapse: collapse;
  margin: 1em 2em;
}
.rendered_html td,
.rendered_html th {
  text-align: left;
  vertical-align: middle;
  padding: 4px;
}
.rendered_html th {
  font-weight: bold;
}
.rendered_html * + table {
  margin-top: 1em;
}
.rendered_html p {
  text-align: left;
}
.rendered_html * + p {
  margin-top: 1em;
}
.rendered_html img {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.rendered_html * + img {
  margin-top: 1em;
}
.rendered_html img,
.rendered_html svg {
  max-width: 100%;
  height: auto;
}
.rendered_html img.unconfined,
.rendered_html svg.unconfined {
  max-width: none;
}
div.text_cell {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.text_cell > div.prompt {
    display: none;
  }
}
div.text_cell_render {
  /*font-family: "Helvetica Neue", Arial, Helvetica, Geneva, sans-serif;*/
  outline: none;
  resize: none;
  width: inherit;
  border-style: none;
  padding: 0.5em 0.5em 0.5em 0.4em;
  color: #000;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
a.anchor-link:link {
  text-decoration: none;
  padding: 0px 20px;
  visibility: hidden;
}
h1:hover .anchor-link,
h2:hover .anchor-link,
h3:hover .anchor-link,
h4:hover .anchor-link,
h5:hover .anchor-link,
h6:hover .anchor-link {
  visibility: visible;
}
.text_cell.rendered .input_area {
  display: none;
}
.text_cell.rendered .rendered_html {
  overflow-x: auto;
  overflow-y: hidden;
}
.text_cell.unrendered .text_cell_render {
  display: none;
}
.cm-header-1,
.cm-header-2,
.cm-header-3,
.cm-header-4,
.cm-header-5,
.cm-header-6 {
  font-weight: bold;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
}
.cm-header-1 {
  font-size: 185.7%;
}
.cm-header-2 {
  font-size: 157.1%;
}
.cm-header-3 {
  font-size: 128.6%;
}
.cm-header-4 {
  font-size: 110%;
}
.cm-header-5 {
  font-size: 100%;
  font-style: italic;
}
.cm-header-6 {
  font-size: 100%;
  font-style: italic;
}
/*!
*
* IPython notebook webapp
*
*/
@media (max-width: 767px) {
  .notebook_app {
    padding-left: 0px;
    padding-right: 0px;
  }
}
#ipython-main-app {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  height: 100%;
}
div#notebook_panel {
  margin: 0px;
  padding: 0px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  height: 100%;
}
div#notebook {
  font-size: 14px;
  line-height: 20px;
  overflow-y: hidden;
  overflow-x: auto;
  width: 100%;
  /* This spaces the page away from the edge of the notebook area */
  padding-top: 20px;
  margin: 0px;
  outline: none;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  min-height: 100%;
}
@media not print {
  #notebook-container {
    padding: 15px;
    background-color: #fff;
    min-height: 0;
    -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
    box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  }
}
@media print {
  #notebook-container {
    width: 100%;
  }
}
div.ui-widget-content {
  border: 1px solid #ababab;
  outline: none;
}
pre.dialog {
  background-color: #f7f7f7;
  border: 1px solid #ddd;
  border-radius: 2px;
  padding: 0.4em;
  padding-left: 2em;
}
p.dialog {
  padding: 0.2em;
}
/* Word-wrap output correctly.  This is the CSS3 spelling, though Firefox seems
   to not honor it correctly.  Webkit browsers (Chrome, rekonq, Safari) do.
 */
pre,
code,
kbd,
samp {
  white-space: pre-wrap;
}
#fonttest {
  font-family: monospace;
}
p {
  margin-bottom: 0;
}
.end_space {
  min-height: 100px;
  transition: height .2s ease;
}
.notebook_app > #header {
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
@media not print {
  .notebook_app {
    background-color: #EEE;
  }
}
kbd {
  border-style: solid;
  border-width: 1px;
  box-shadow: none;
  margin: 2px;
  padding-left: 2px;
  padding-right: 2px;
  padding-top: 1px;
  padding-bottom: 1px;
}
/* CSS for the cell toolbar */
.celltoolbar {
  border: thin solid #CFCFCF;
  border-bottom: none;
  background: #EEE;
  border-radius: 2px 2px 0px 0px;
  width: 100%;
  height: 29px;
  padding-right: 4px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
  /* Old browsers */
  -webkit-box-pack: end;
  -moz-box-pack: end;
  box-pack: end;
  /* Modern browsers */
  justify-content: flex-end;
  display: -webkit-flex;
}
@media print {
  .celltoolbar {
    display: none;
  }
}
.ctb_hideshow {
  display: none;
  vertical-align: bottom;
}
/* ctb_show is added to the ctb_hideshow div to show the cell toolbar.
   Cell toolbars are only shown when the ctb_global_show class is also set.
*/
.ctb_global_show .ctb_show.ctb_hideshow {
  display: block;
}
.ctb_global_show .ctb_show + .input_area,
.ctb_global_show .ctb_show + div.text_cell_input,
.ctb_global_show .ctb_show ~ div.text_cell_render {
  border-top-right-radius: 0px;
  border-top-left-radius: 0px;
}
.ctb_global_show .ctb_show ~ div.text_cell_render {
  border: 1px solid #cfcfcf;
}
.celltoolbar {
  font-size: 87%;
  padding-top: 3px;
}
.celltoolbar select {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
  width: inherit;
  font-size: inherit;
  height: 22px;
  padding: 0px;
  display: inline-block;
}
.celltoolbar select:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.celltoolbar select::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.celltoolbar select:-ms-input-placeholder {
  color: #999;
}
.celltoolbar select::-webkit-input-placeholder {
  color: #999;
}
.celltoolbar select::-ms-expand {
  border: 0;
  background-color: transparent;
}
.celltoolbar select[disabled],
.celltoolbar select[readonly],
fieldset[disabled] .celltoolbar select {
  background-color: #eeeeee;
  opacity: 1;
}
.celltoolbar select[disabled],
fieldset[disabled] .celltoolbar select {
  cursor: not-allowed;
}
textarea.celltoolbar select {
  height: auto;
}
select.celltoolbar select {
  height: 30px;
  line-height: 30px;
}
textarea.celltoolbar select,
select[multiple].celltoolbar select {
  height: auto;
}
.celltoolbar label {
  margin-left: 5px;
  margin-right: 5px;
}
.completions {
  position: absolute;
  z-index: 110;
  overflow: hidden;
  border: 1px solid #ababab;
  border-radius: 2px;
  -webkit-box-shadow: 0px 6px 10px -1px #adadad;
  box-shadow: 0px 6px 10px -1px #adadad;
  line-height: 1;
}
.completions select {
  background: white;
  outline: none;
  border: none;
  padding: 0px;
  margin: 0px;
  overflow: auto;
  font-family: monospace;
  font-size: 110%;
  color: #000;
  width: auto;
}
.completions select option.context {
  color: #286090;
}
#kernel_logo_widget {
  float: right !important;
  float: right;
}
#kernel_logo_widget .current_kernel_logo {
  display: none;
  margin-top: -1px;
  margin-bottom: -1px;
  width: 32px;
  height: 32px;
}
#menubar {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  margin-top: 1px;
}
#menubar .navbar {
  border-top: 1px;
  border-radius: 0px 0px 2px 2px;
  margin-bottom: 0px;
}
#menubar .navbar-toggle {
  float: left;
  padding-top: 7px;
  padding-bottom: 7px;
  border: none;
}
#menubar .navbar-collapse {
  clear: left;
}
.nav-wrapper {
  border-bottom: 1px solid #e7e7e7;
}
i.menu-icon {
  padding-top: 4px;
}
ul#help_menu li a {
  overflow: hidden;
  padding-right: 2.2em;
}
ul#help_menu li a i {
  margin-right: -1.2em;
}
.dropdown-submenu {
  position: relative;
}
.dropdown-submenu > .dropdown-menu {
  top: 0;
  left: 100%;
  margin-top: -6px;
  margin-left: -1px;
}
.dropdown-submenu:hover > .dropdown-menu {
  display: block;
}
.dropdown-submenu > a:after {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  display: block;
  content: "\f0da";
  float: right;
  color: #333333;
  margin-top: 2px;
  margin-right: -10px;
}
.dropdown-submenu > a:after.pull-left {
  margin-right: .3em;
}
.dropdown-submenu > a:after.pull-right {
  margin-left: .3em;
}
.dropdown-submenu:hover > a:after {
  color: #262626;
}
.dropdown-submenu.pull-left {
  float: none;
}
.dropdown-submenu.pull-left > .dropdown-menu {
  left: -100%;
  margin-left: 10px;
}
#notification_area {
  float: right !important;
  float: right;
  z-index: 10;
}
.indicator_area {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
}
#kernel_indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
  border-left: 1px solid;
}
#kernel_indicator .kernel_indicator_name {
  padding-left: 5px;
  padding-right: 5px;
}
#modal_indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
}
#readonly-indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
  margin-top: 2px;
  margin-bottom: 0px;
  margin-left: 0px;
  margin-right: 0px;
  display: none;
}
.modal_indicator:before {
  width: 1.28571429em;
  text-align: center;
}
.edit_mode .modal_indicator:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f040";
}
.edit_mode .modal_indicator:before.pull-left {
  margin-right: .3em;
}
.edit_mode .modal_indicator:before.pull-right {
  margin-left: .3em;
}
.command_mode .modal_indicator:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: ' ';
}
.command_mode .modal_indicator:before.pull-left {
  margin-right: .3em;
}
.command_mode .modal_indicator:before.pull-right {
  margin-left: .3em;
}
.kernel_idle_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f10c";
}
.kernel_idle_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_idle_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_busy_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f111";
}
.kernel_busy_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_busy_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_dead_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f1e2";
}
.kernel_dead_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_dead_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_disconnected_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f127";
}
.kernel_disconnected_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_disconnected_icon:before.pull-right {
  margin-left: .3em;
}
.notification_widget {
  color: #777;
  z-index: 10;
  background: rgba(240, 240, 240, 0.5);
  margin-right: 4px;
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
.notification_widget:focus,
.notification_widget.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
.notification_widget:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.notification_widget:active,
.notification_widget.active,
.open > .dropdown-toggle.notification_widget {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.notification_widget:active:hover,
.notification_widget.active:hover,
.open > .dropdown-toggle.notification_widget:hover,
.notification_widget:active:focus,
.notification_widget.active:focus,
.open > .dropdown-toggle.notification_widget:focus,
.notification_widget:active.focus,
.notification_widget.active.focus,
.open > .dropdown-toggle.notification_widget.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
.notification_widget:active,
.notification_widget.active,
.open > .dropdown-toggle.notification_widget {
  background-image: none;
}
.notification_widget.disabled:hover,
.notification_widget[disabled]:hover,
fieldset[disabled] .notification_widget:hover,
.notification_widget.disabled:focus,
.notification_widget[disabled]:focus,
fieldset[disabled] .notification_widget:focus,
.notification_widget.disabled.focus,
.notification_widget[disabled].focus,
fieldset[disabled] .notification_widget.focus {
  background-color: #fff;
  border-color: #ccc;
}
.notification_widget .badge {
  color: #fff;
  background-color: #333;
}
.notification_widget.warning {
  color: #fff;
  background-color: #f0ad4e;
  border-color: #eea236;
}
.notification_widget.warning:focus,
.notification_widget.warning.focus {
  color: #fff;
  background-color: #ec971f;
  border-color: #985f0d;
}
.notification_widget.warning:hover {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.notification_widget.warning:active,
.notification_widget.warning.active,
.open > .dropdown-toggle.notification_widget.warning {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.notification_widget.warning:active:hover,
.notification_widget.warning.active:hover,
.open > .dropdown-toggle.notification_widget.warning:hover,
.notification_widget.warning:active:focus,
.notification_widget.warning.active:focus,
.open > .dropdown-toggle.notification_widget.warning:focus,
.notification_widget.warning:active.focus,
.notification_widget.warning.active.focus,
.open > .dropdown-toggle.notification_widget.warning.focus {
  color: #fff;
  background-color: #d58512;
  border-color: #985f0d;
}
.notification_widget.warning:active,
.notification_widget.warning.active,
.open > .dropdown-toggle.notification_widget.warning {
  background-image: none;
}
.notification_widget.warning.disabled:hover,
.notification_widget.warning[disabled]:hover,
fieldset[disabled] .notification_widget.warning:hover,
.notification_widget.warning.disabled:focus,
.notification_widget.warning[disabled]:focus,
fieldset[disabled] .notification_widget.warning:focus,
.notification_widget.warning.disabled.focus,
.notification_widget.warning[disabled].focus,
fieldset[disabled] .notification_widget.warning.focus {
  background-color: #f0ad4e;
  border-color: #eea236;
}
.notification_widget.warning .badge {
  color: #f0ad4e;
  background-color: #fff;
}
.notification_widget.success {
  color: #fff;
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.notification_widget.success:focus,
.notification_widget.success.focus {
  color: #fff;
  background-color: #449d44;
  border-color: #255625;
}
.notification_widget.success:hover {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.notification_widget.success:active,
.notification_widget.success.active,
.open > .dropdown-toggle.notification_widget.success {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.notification_widget.success:active:hover,
.notification_widget.success.active:hover,
.open > .dropdown-toggle.notification_widget.success:hover,
.notification_widget.success:active:focus,
.notification_widget.success.active:focus,
.open > .dropdown-toggle.notification_widget.success:focus,
.notification_widget.success:active.focus,
.notification_widget.success.active.focus,
.open > .dropdown-toggle.notification_widget.success.focus {
  color: #fff;
  background-color: #398439;
  border-color: #255625;
}
.notification_widget.success:active,
.notification_widget.success.active,
.open > .dropdown-toggle.notification_widget.success {
  background-image: none;
}
.notification_widget.success.disabled:hover,
.notification_widget.success[disabled]:hover,
fieldset[disabled] .notification_widget.success:hover,
.notification_widget.success.disabled:focus,
.notification_widget.success[disabled]:focus,
fieldset[disabled] .notification_widget.success:focus,
.notification_widget.success.disabled.focus,
.notification_widget.success[disabled].focus,
fieldset[disabled] .notification_widget.success.focus {
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.notification_widget.success .badge {
  color: #5cb85c;
  background-color: #fff;
}
.notification_widget.info {
  color: #fff;
  background-color: #5bc0de;
  border-color: #46b8da;
}
.notification_widget.info:focus,
.notification_widget.info.focus {
  color: #fff;
  background-color: #31b0d5;
  border-color: #1b6d85;
}
.notification_widget.info:hover {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.notification_widget.info:active,
.notification_widget.info.active,
.open > .dropdown-toggle.notification_widget.info {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.notification_widget.info:active:hover,
.notification_widget.info.active:hover,
.open > .dropdown-toggle.notification_widget.info:hover,
.notification_widget.info:active:focus,
.notification_widget.info.active:focus,
.open > .dropdown-toggle.notification_widget.info:focus,
.notification_widget.info:active.focus,
.notification_widget.info.active.focus,
.open > .dropdown-toggle.notification_widget.info.focus {
  color: #fff;
  background-color: #269abc;
  border-color: #1b6d85;
}
.notification_widget.info:active,
.notification_widget.info.active,
.open > .dropdown-toggle.notification_widget.info {
  background-image: none;
}
.notification_widget.info.disabled:hover,
.notification_widget.info[disabled]:hover,
fieldset[disabled] .notification_widget.info:hover,
.notification_widget.info.disabled:focus,
.notification_widget.info[disabled]:focus,
fieldset[disabled] .notification_widget.info:focus,
.notification_widget.info.disabled.focus,
.notification_widget.info[disabled].focus,
fieldset[disabled] .notification_widget.info.focus {
  background-color: #5bc0de;
  border-color: #46b8da;
}
.notification_widget.info .badge {
  color: #5bc0de;
  background-color: #fff;
}
.notification_widget.danger {
  color: #fff;
  background-color: #d9534f;
  border-color: #d43f3a;
}
.notification_widget.danger:focus,
.notification_widget.danger.focus {
  color: #fff;
  background-color: #c9302c;
  border-color: #761c19;
}
.notification_widget.danger:hover {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.notification_widget.danger:active,
.notification_widget.danger.active,
.open > .dropdown-toggle.notification_widget.danger {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.notification_widget.danger:active:hover,
.notification_widget.danger.active:hover,
.open > .dropdown-toggle.notification_widget.danger:hover,
.notification_widget.danger:active:focus,
.notification_widget.danger.active:focus,
.open > .dropdown-toggle.notification_widget.danger:focus,
.notification_widget.danger:active.focus,
.notification_widget.danger.active.focus,
.open > .dropdown-toggle.notification_widget.danger.focus {
  color: #fff;
  background-color: #ac2925;
  border-color: #761c19;
}
.notification_widget.danger:active,
.notification_widget.danger.active,
.open > .dropdown-toggle.notification_widget.danger {
  background-image: none;
}
.notification_widget.danger.disabled:hover,
.notification_widget.danger[disabled]:hover,
fieldset[disabled] .notification_widget.danger:hover,
.notification_widget.danger.disabled:focus,
.notification_widget.danger[disabled]:focus,
fieldset[disabled] .notification_widget.danger:focus,
.notification_widget.danger.disabled.focus,
.notification_widget.danger[disabled].focus,
fieldset[disabled] .notification_widget.danger.focus {
  background-color: #d9534f;
  border-color: #d43f3a;
}
.notification_widget.danger .badge {
  color: #d9534f;
  background-color: #fff;
}
div#pager {
  background-color: #fff;
  font-size: 14px;
  line-height: 20px;
  overflow: hidden;
  display: none;
  position: fixed;
  bottom: 0px;
  width: 100%;
  max-height: 50%;
  padding-top: 8px;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  /* Display over codemirror */
  z-index: 100;
  /* Hack which prevents jquery ui resizable from changing top. */
  top: auto !important;
}
div#pager pre {
  line-height: 1.21429em;
  color: #000;
  background-color: #f7f7f7;
  padding: 0.4em;
}
div#pager #pager-button-area {
  position: absolute;
  top: 8px;
  right: 20px;
}
div#pager #pager-contents {
  position: relative;
  overflow: auto;
  width: 100%;
  height: 100%;
}
div#pager #pager-contents #pager-container {
  position: relative;
  padding: 15px 0px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
div#pager .ui-resizable-handle {
  top: 0px;
  height: 8px;
  background: #f7f7f7;
  border-top: 1px solid #cfcfcf;
  border-bottom: 1px solid #cfcfcf;
  /* This injects handle bars (a short, wide = symbol) for 
        the resize handle. */
}
div#pager .ui-resizable-handle::after {
  content: '';
  top: 2px;
  left: 50%;
  height: 3px;
  width: 30px;
  margin-left: -15px;
  position: absolute;
  border-top: 1px solid #cfcfcf;
}
.quickhelp {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
  line-height: 1.8em;
}
.shortcut_key {
  display: inline-block;
  width: 21ex;
  text-align: right;
  font-family: monospace;
}
.shortcut_descr {
  display: inline-block;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
span.save_widget {
  margin-top: 6px;
}
span.save_widget span.filename {
  height: 1em;
  line-height: 1em;
  padding: 3px;
  margin-left: 16px;
  border: none;
  font-size: 146.5%;
  border-radius: 2px;
}
span.save_widget span.filename:hover {
  background-color: #e6e6e6;
}
span.checkpoint_status,
span.autosave_status {
  font-size: small;
}
@media (max-width: 767px) {
  span.save_widget {
    font-size: small;
  }
  span.checkpoint_status,
  span.autosave_status {
    display: none;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  span.checkpoint_status {
    display: none;
  }
  span.autosave_status {
    font-size: x-small;
  }
}
.toolbar {
  padding: 0px;
  margin-left: -5px;
  margin-top: 2px;
  margin-bottom: 5px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
.toolbar select,
.toolbar label {
  width: auto;
  vertical-align: middle;
  margin-right: 2px;
  margin-bottom: 0px;
  display: inline;
  font-size: 92%;
  margin-left: 0.3em;
  margin-right: 0.3em;
  padding: 0px;
  padding-top: 3px;
}
.toolbar .btn {
  padding: 2px 8px;
}
.toolbar .btn-group {
  margin-top: 0px;
  margin-left: 5px;
}
#maintoolbar {
  margin-bottom: -3px;
  margin-top: -8px;
  border: 0px;
  min-height: 27px;
  margin-left: 0px;
  padding-top: 11px;
  padding-bottom: 3px;
}
#maintoolbar .navbar-text {
  float: none;
  vertical-align: middle;
  text-align: right;
  margin-left: 5px;
  margin-right: 0px;
  margin-top: 0px;
}
.select-xs {
  height: 24px;
}
.pulse,
.dropdown-menu > li > a.pulse,
li.pulse > a.dropdown-toggle,
li.pulse.open > a.dropdown-toggle {
  background-color: #F37626;
  color: white;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
/** WARNING IF YOU ARE EDITTING THIS FILE, if this is a .css file, It has a lot
 * of chance of beeing generated from the ../less/[samename].less file, you can
 * try to get back the less file by reverting somme commit in history
 **/
/*
 * We'll try to get something pretty, so we
 * have some strange css to have the scroll bar on
 * the left with fix button on the top right of the tooltip
 */
@-moz-keyframes fadeOut {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}
@-webkit-keyframes fadeOut {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}
@-moz-keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
@-webkit-keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
/*properties of tooltip after "expand"*/
.bigtooltip {
  overflow: auto;
  height: 200px;
  -webkit-transition-property: height;
  -webkit-transition-duration: 500ms;
  -moz-transition-property: height;
  -moz-transition-duration: 500ms;
  transition-property: height;
  transition-duration: 500ms;
}
/*properties of tooltip before "expand"*/
.smalltooltip {
  -webkit-transition-property: height;
  -webkit-transition-duration: 500ms;
  -moz-transition-property: height;
  -moz-transition-duration: 500ms;
  transition-property: height;
  transition-duration: 500ms;
  text-overflow: ellipsis;
  overflow: hidden;
  height: 80px;
}
.tooltipbuttons {
  position: absolute;
  padding-right: 15px;
  top: 0px;
  right: 0px;
}
.tooltiptext {
  /*avoid the button to overlap on some docstring*/
  padding-right: 30px;
}
.ipython_tooltip {
  max-width: 700px;
  /*fade-in animation when inserted*/
  -webkit-animation: fadeOut 400ms;
  -moz-animation: fadeOut 400ms;
  animation: fadeOut 400ms;
  -webkit-animation: fadeIn 400ms;
  -moz-animation: fadeIn 400ms;
  animation: fadeIn 400ms;
  vertical-align: middle;
  background-color: #f7f7f7;
  overflow: visible;
  border: #ababab 1px solid;
  outline: none;
  padding: 3px;
  margin: 0px;
  padding-left: 7px;
  font-family: monospace;
  min-height: 50px;
  -moz-box-shadow: 0px 6px 10px -1px #adadad;
  -webkit-box-shadow: 0px 6px 10px -1px #adadad;
  box-shadow: 0px 6px 10px -1px #adadad;
  border-radius: 2px;
  position: absolute;
  z-index: 1000;
}
.ipython_tooltip a {
  float: right;
}
.ipython_tooltip .tooltiptext pre {
  border: 0;
  border-radius: 0;
  font-size: 100%;
  background-color: #f7f7f7;
}
.pretooltiparrow {
  left: 0px;
  margin: 0px;
  top: -16px;
  width: 40px;
  height: 16px;
  overflow: hidden;
  position: absolute;
}
.pretooltiparrow:before {
  background-color: #f7f7f7;
  border: 1px #ababab solid;
  z-index: 11;
  content: "";
  position: absolute;
  left: 15px;
  top: 10px;
  width: 25px;
  height: 25px;
  -webkit-transform: rotate(45deg);
  -moz-transform: rotate(45deg);
  -ms-transform: rotate(45deg);
  -o-transform: rotate(45deg);
}
ul.typeahead-list i {
  margin-left: -10px;
  width: 18px;
}
ul.typeahead-list {
  max-height: 80vh;
  overflow: auto;
}
ul.typeahead-list > li > a {
  /** Firefox bug **/
  /* see https://github.com/jupyter/notebook/issues/559 */
  white-space: normal;
}
.cmd-palette .modal-body {
  padding: 7px;
}
.cmd-palette form {
  background: white;
}
.cmd-palette input {
  outline: none;
}
.no-shortcut {
  display: none;
}
.command-shortcut:before {
  content: "(command)";
  padding-right: 3px;
  color: #777777;
}
.edit-shortcut:before {
  content: "(edit)";
  padding-right: 3px;
  color: #777777;
}
#find-and-replace #replace-preview .match,
#find-and-replace #replace-preview .insert {
  background-color: #BBDEFB;
  border-color: #90CAF9;
  border-style: solid;
  border-width: 1px;
  border-radius: 0px;
}
#find-and-replace #replace-preview .replace .match {
  background-color: #FFCDD2;
  border-color: #EF9A9A;
  border-radius: 0px;
}
#find-and-replace #replace-preview .replace .insert {
  background-color: #C8E6C9;
  border-color: #A5D6A7;
  border-radius: 0px;
}
#find-and-replace #replace-preview {
  max-height: 60vh;
  overflow: auto;
}
#find-and-replace #replace-preview pre {
  padding: 5px 10px;
}
.terminal-app {
  background: #EEE;
}
.terminal-app #header {
  background: #fff;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
.terminal-app .terminal {
  width: 100%;
  float: left;
  font-family: monospace;
  color: white;
  background: black;
  padding: 0.4em;
  border-radius: 2px;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.4);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.4);
}
.terminal-app .terminal,
.terminal-app .terminal dummy-screen {
  line-height: 1em;
  font-size: 14px;
}
.terminal-app .terminal .xterm-rows {
  padding: 10px;
}
.terminal-app .terminal-cursor {
  color: black;
  background: white;
}
.terminal-app #terminado-container {
  margin-top: 20px;
}
/*# sourceMappingURL=style.min.css.map */
    </style>
<style type="text/css">
    .highlight .hll { background-color: #ffffcc }
.highlight  { background: #f8f8f8; }
.highlight .c { color: #408080; font-style: italic } /* Comment */
.highlight .err { border: 1px solid #FF0000 } /* Error */
.highlight .k { color: #008000; font-weight: bold } /* Keyword */
.highlight .o { color: #666666 } /* Operator */
.highlight .ch { color: #408080; font-style: italic } /* Comment.Hashbang */
.highlight .cm { color: #408080; font-style: italic } /* Comment.Multiline */
.highlight .cp { color: #BC7A00 } /* Comment.Preproc */
.highlight .cpf { color: #408080; font-style: italic } /* Comment.PreprocFile */
.highlight .c1 { color: #408080; font-style: italic } /* Comment.Single */
.highlight .cs { color: #408080; font-style: italic } /* Comment.Special */
.highlight .gd { color: #A00000 } /* Generic.Deleted */
.highlight .ge { font-style: italic } /* Generic.Emph */
.highlight .gr { color: #FF0000 } /* Generic.Error */
.highlight .gh { color: #000080; font-weight: bold } /* Generic.Heading */
.highlight .gi { color: #00A000 } /* Generic.Inserted */
.highlight .go { color: #888888 } /* Generic.Output */
.highlight .gp { color: #000080; font-weight: bold } /* Generic.Prompt */
.highlight .gs { font-weight: bold } /* Generic.Strong */
.highlight .gu { color: #800080; font-weight: bold } /* Generic.Subheading */
.highlight .gt { color: #0044DD } /* Generic.Traceback */
.highlight .kc { color: #008000; font-weight: bold } /* Keyword.Constant */
.highlight .kd { color: #008000; font-weight: bold } /* Keyword.Declaration */
.highlight .kn { color: #008000; font-weight: bold } /* Keyword.Namespace */
.highlight .kp { color: #008000 } /* Keyword.Pseudo */
.highlight .kr { color: #008000; font-weight: bold } /* Keyword.Reserved */
.highlight .kt { color: #B00040 } /* Keyword.Type */
.highlight .m { color: #666666 } /* Literal.Number */
.highlight .s { color: #BA2121 } /* Literal.String */
.highlight .na { color: #7D9029 } /* Name.Attribute */
.highlight .nb { color: #008000 } /* Name.Builtin */
.highlight .nc { color: #0000FF; font-weight: bold } /* Name.Class */
.highlight .no { color: #880000 } /* Name.Constant */
.highlight .nd { color: #AA22FF } /* Name.Decorator */
.highlight .ni { color: #999999; font-weight: bold } /* Name.Entity */
.highlight .ne { color: #D2413A; font-weight: bold } /* Name.Exception */
.highlight .nf { color: #0000FF } /* Name.Function */
.highlight .nl { color: #A0A000 } /* Name.Label */
.highlight .nn { color: #0000FF; font-weight: bold } /* Name.Namespace */
.highlight .nt { color: #008000; font-weight: bold } /* Name.Tag */
.highlight .nv { color: #19177C } /* Name.Variable */
.highlight .ow { color: #AA22FF; font-weight: bold } /* Operator.Word */
.highlight .w { color: #bbbbbb } /* Text.Whitespace */
.highlight .mb { color: #666666 } /* Literal.Number.Bin */
.highlight .mf { color: #666666 } /* Literal.Number.Float */
.highlight .mh { color: #666666 } /* Literal.Number.Hex */
.highlight .mi { color: #666666 } /* Literal.Number.Integer */
.highlight .mo { color: #666666 } /* Literal.Number.Oct */
.highlight .sa { color: #BA2121 } /* Literal.String.Affix */
.highlight .sb { color: #BA2121 } /* Literal.String.Backtick */
.highlight .sc { color: #BA2121 } /* Literal.String.Char */
.highlight .dl { color: #BA2121 } /* Literal.String.Delimiter */
.highlight .sd { color: #BA2121; font-style: italic } /* Literal.String.Doc */
.highlight .s2 { color: #BA2121 } /* Literal.String.Double */
.highlight .se { color: #BB6622; font-weight: bold } /* Literal.String.Escape */
.highlight .sh { color: #BA2121 } /* Literal.String.Heredoc */
.highlight .si { color: #BB6688; font-weight: bold } /* Literal.String.Interpol */
.highlight .sx { color: #008000 } /* Literal.String.Other */
.highlight .sr { color: #BB6688 } /* Literal.String.Regex */
.highlight .s1 { color: #BA2121 } /* Literal.String.Single */
.highlight .ss { color: #19177C } /* Literal.String.Symbol */
.highlight .bp { color: #008000 } /* Name.Builtin.Pseudo */
.highlight .fm { color: #0000FF } /* Name.Function.Magic */
.highlight .vc { color: #19177C } /* Name.Variable.Class */
.highlight .vg { color: #19177C } /* Name.Variable.Global */
.highlight .vi { color: #19177C } /* Name.Variable.Instance */
.highlight .vm { color: #19177C } /* Name.Variable.Magic */
.highlight .il { color: #666666 } /* Literal.Number.Integer.Long */
    </style>
<style type="text/css">
    
/* Temporary definitions which will become obsolete with Notebook release 5.0 */
.ansi-black-fg { color: #3E424D; }
.ansi-black-bg { background-color: #3E424D; }
.ansi-black-intense-fg { color: #282C36; }
.ansi-black-intense-bg { background-color: #282C36; }
.ansi-red-fg { color: #E75C58; }
.ansi-red-bg { background-color: #E75C58; }
.ansi-red-intense-fg { color: #B22B31; }
.ansi-red-intense-bg { background-color: #B22B31; }
.ansi-green-fg { color: #00A250; }
.ansi-green-bg { background-color: #00A250; }
.ansi-green-intense-fg { color: #007427; }
.ansi-green-intense-bg { background-color: #007427; }
.ansi-yellow-fg { color: #DDB62B; }
.ansi-yellow-bg { background-color: #DDB62B; }
.ansi-yellow-intense-fg { color: #B27D12; }
.ansi-yellow-intense-bg { background-color: #B27D12; }
.ansi-blue-fg { color: #208FFB; }
.ansi-blue-bg { background-color: #208FFB; }
.ansi-blue-intense-fg { color: #0065CA; }
.ansi-blue-intense-bg { background-color: #0065CA; }
.ansi-magenta-fg { color: #D160C4; }
.ansi-magenta-bg { background-color: #D160C4; }
.ansi-magenta-intense-fg { color: #A03196; }
.ansi-magenta-intense-bg { background-color: #A03196; }
.ansi-cyan-fg { color: #60C6C8; }
.ansi-cyan-bg { background-color: #60C6C8; }
.ansi-cyan-intense-fg { color: #258F8F; }
.ansi-cyan-intense-bg { background-color: #258F8F; }
.ansi-white-fg { color: #C5C1B4; }
.ansi-white-bg { background-color: #C5C1B4; }
.ansi-white-intense-fg { color: #A1A6B2; }
.ansi-white-intense-bg { background-color: #A1A6B2; }

.ansi-bold { font-weight: bold; }

    </style>


<style type="text/css">
/* Overrides of notebook CSS for static HTML export */
body {
  overflow: visible;
  padding: 8px;
}

div#notebook {
  overflow: visible;
  border-top: none;
}@media print {
  div.cell {
    display: block;
    page-break-inside: avoid;
  } 
  div.output_wrapper { 
    display: block;
    page-break-inside: avoid; 
  }
  div.output { 
    display: block;
    page-break-inside: avoid; 
  }
}
</style>

<!-- Custom stylesheet, it must be in the same directory as the html file -->
<link rel="stylesheet" href="custom.css">

<!-- Loading mathjax macro -->
<!-- Load mathjax -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS_HTML"></script>
    <!-- MathJax configuration -->
    <script type="text/x-mathjax-config">
    MathJax.Hub.Config({
        tex2jax: {
            inlineMath: [ ['$','$'], ["\\(","\\)"] ],
            displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
            processEscapes: true,
            processEnvironments: true
        },
        // Center justify equations in code and markdown cells. Elsewhere
        // we use CSS to left justify single line equations in code cells.
        displayAlign: 'center',
        "HTML-CSS": {
            styles: {'.MathJax_Display': {"margin": 0}},
            linebreaks: { automatic: true }
        }
    });
    </script>
    <!-- End of mathjax configuration --></head>
<body>
  <div tabindex="-1" id="notebook" class="border-box-sizing">
    <div class="container" id="notebook-container">

<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Self-Driving-Car-Engineer-Nanodegree">Self-Driving Car Engineer Nanodegree<a class="anchor-link" href="#Self-Driving-Car-Engineer-Nanodegree">&#182;</a></h1><h2 id="Deep-Learning">Deep Learning<a class="anchor-link" href="#Deep-Learning">&#182;</a></h2><h2 id="Project:-Build-a-Traffic-Sign-Recognition-Classifier">Project: Build a Traffic Sign Recognition Classifier<a class="anchor-link" href="#Project:-Build-a-Traffic-Sign-Recognition-Classifier">&#182;</a></h2><p>In this notebook, a template is provided for you to implement your functionality in stages, which is required to successfully complete this project. If additional code is required that cannot be included in the notebook, be sure that the Python code is successfully imported and included in your submission if necessary.</p>
<blockquote><p><strong>Note</strong>: Once you have completed all of the code implementations, you need to finalize your work by exporting the iPython Notebook as an HTML document. Before exporting the notebook to html, all of the code cells need to have been run so that reviewers can see the final implementation and output. You can then export the notebook by using the menu above and navigating to  \n",
    "<strong>File -&gt; Download as -&gt; HTML (.html)</strong>. Include the finished document along with this notebook as your submission.</p>
</blockquote>
<p>In addition to implementing code, there is a writeup to complete. The writeup should be completed in a separate file, which can be either a markdown file or a pdf document. There is a <a href="https://github.com/udacity/CarND-Traffic-Sign-Classifier-Project/blob/master/writeup_template.md">write up template</a> that can be used to guide the writing process. Completing the code template and writeup template will cover all of the <a href="https://review.udacity.com/#!/rubrics/481/view">rubric points</a> for this project.</p>
<p>The <a href="https://review.udacity.com/#!/rubrics/481/view">rubric</a> contains "Stand Out Suggestions" for enhancing the project beyond the minimum requirements. The stand out suggestions are optional. If you decide to pursue the "stand out suggestions", you can include the code in this Ipython notebook and also discuss the results in the writeup file.</p>
<blockquote><p><strong>Note:</strong> Code and Markdown cells can be executed using the <strong>Shift + Enter</strong> keyboard shortcut. In addition, Markdown cells can be edited by typically double-clicking the cell to enter edit mode.</p>
</blockquote>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<hr>
<h2 id="Step-0:-Load-The-Data">Step 0: Load The Data<a class="anchor-link" href="#Step-0:-Load-The-Data">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[26]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Load pickled data</span>
<span class="kn">import</span> <span class="nn">pickle</span>
<span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
<span class="kn">import</span> <span class="nn">tensorflow</span> <span class="k">as</span> <span class="nn">tf</span>
<span class="c1"># TODO: Fill this in based on where you saved the training and testing data</span>

<span class="n">training_file</span> <span class="o">=</span> <span class="s1">&#39;train.p&#39;</span>
<span class="n">validation_file</span> <span class="o">=</span> <span class="s1">&#39;valid.p&#39;</span>
<span class="n">testing_file</span> <span class="o">=</span> <span class="s1">&#39;test.p&#39;</span>

<span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">training_file</span><span class="p">,</span> <span class="n">mode</span><span class="o">=</span><span class="s1">&#39;rb&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
    <span class="n">train</span> <span class="o">=</span> <span class="n">pickle</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="n">f</span><span class="p">)</span>
<span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">validation_file</span><span class="p">,</span> <span class="n">mode</span><span class="o">=</span><span class="s1">&#39;rb&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
    <span class="n">valid</span> <span class="o">=</span> <span class="n">pickle</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="n">f</span><span class="p">)</span>
<span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">testing_file</span><span class="p">,</span> <span class="n">mode</span><span class="o">=</span><span class="s1">&#39;rb&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
    <span class="n">test</span> <span class="o">=</span> <span class="n">pickle</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="n">f</span><span class="p">)</span>
    
<span class="n">X_train</span><span class="p">,</span> <span class="n">y_train</span> <span class="o">=</span> <span class="n">train</span><span class="p">[</span><span class="s1">&#39;features&#39;</span><span class="p">],</span> <span class="n">train</span><span class="p">[</span><span class="s1">&#39;labels&#39;</span><span class="p">]</span>
<span class="n">X_valid</span><span class="p">,</span> <span class="n">y_valid</span> <span class="o">=</span> <span class="n">valid</span><span class="p">[</span><span class="s1">&#39;features&#39;</span><span class="p">],</span> <span class="n">valid</span><span class="p">[</span><span class="s1">&#39;labels&#39;</span><span class="p">]</span>
<span class="n">X_test</span><span class="p">,</span> <span class="n">y_test</span> <span class="o">=</span> <span class="n">test</span><span class="p">[</span><span class="s1">&#39;features&#39;</span><span class="p">],</span> <span class="n">test</span><span class="p">[</span><span class="s1">&#39;labels&#39;</span><span class="p">]</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<hr>
<h2 id="Step-1:-Dataset-Summary-&amp;-Exploration">Step 1: Dataset Summary &amp; Exploration<a class="anchor-link" href="#Step-1:-Dataset-Summary-&amp;-Exploration">&#182;</a></h2><p>The pickled data is a dictionary with 4 key/value pairs:</p>
<ul>
<li><code>'features'</code> is a 4D array containing raw pixel data of the traffic sign images, (num examples, width, height, channels).</li>
<li><code>'labels'</code> is a 1D array containing the label/class id of the traffic sign. The file <code>signnames.csv</code> contains id -&gt; name mappings for each id.</li>
<li><code>'sizes'</code> is a list containing tuples, (width, height) representing the original width and height the image.</li>
<li><code>'coords'</code> is a list containing tuples, (x1, y1, x2, y2) representing coordinates of a bounding box around the sign in the image. <strong>THESE COORDINATES ASSUME THE ORIGINAL IMAGE. THE PICKLED DATA CONTAINS RESIZED VERSIONS (32 by 32) OF THESE IMAGES</strong></li>
</ul>
<p>Complete the basic data summary below. Use python, numpy and/or pandas methods to calculate the data summary rather than hard coding the results. For example, the <a href="http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.shape.html">pandas shape method</a> might be useful for calculating some of the summary results.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Provide-a-Basic-Summary-of-the-Data-Set-Using-Python,-Numpy-and/or-Pandas">Provide a Basic Summary of the Data Set Using Python, Numpy and/or Pandas<a class="anchor-link" href="#Provide-a-Basic-Summary-of-the-Data-Set-Using-Python,-Numpy-and/or-Pandas">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[27]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">### Replace each question mark with the appropriate value. </span>
<span class="c1">### Use python, pandas or numpy methods rather than hard coding the results</span>

<span class="c1"># TODO: Number of training examples</span>
<span class="n">n_train</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">X_train</span><span class="p">)</span>

<span class="c1"># TODO: Number of validation examples</span>
<span class="n">n_validation</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">X_valid</span><span class="p">)</span>

<span class="c1"># TODO: Number of testing examples.</span>
<span class="n">n_test</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">X_test</span><span class="p">)</span>

<span class="c1"># TODO: What&#39;s the shape of an traffic sign image?</span>
<span class="n">image_shape</span> <span class="o">=</span> <span class="n">X_train</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">shape</span>

<span class="c1"># TODO: How many unique classes/labels there are in the dataset.</span>
<span class="n">n_classes</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">unique</span><span class="p">(</span><span class="n">y_train</span><span class="p">))</span>

<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Number of training examples =&quot;</span><span class="p">,</span> <span class="n">n_train</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Number of validating examples =&quot;</span><span class="p">,</span> <span class="n">n_validation</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Number of testing examples =&quot;</span><span class="p">,</span> <span class="n">n_test</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Image data shape =&quot;</span><span class="p">,</span> <span class="n">image_shape</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Number of classes =&quot;</span><span class="p">,</span> <span class="n">n_classes</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Number of training examples = 34799
Number of validating examples = 4410
Number of testing examples = 12630
Image data shape = (32, 32, 3)
Number of classes = 43
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Include-an-exploratory-visualization-of-the-dataset">Include an exploratory visualization of the dataset<a class="anchor-link" href="#Include-an-exploratory-visualization-of-the-dataset">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Visualize the German Traffic Signs Dataset using the pickled file(s). This is open ended, suggestions include: plotting traffic sign images, plotting the count of each sign, etc.</p>
<p>The <a href="http://matplotlib.org/">Matplotlib</a> <a href="http://matplotlib.org/examples/index.html">examples</a> and <a href="http://matplotlib.org/gallery.html">gallery</a> pages are a great resource for doing visualizations in Python.</p>
<p><strong>NOTE:</strong> It's recommended you start with something simple first. If you wish to do more, come back to it after you've completed the rest of the sections. It can be interesting to look at the distribution of classes in the training, validation and test set. Is the distribution the same? Are there more examples of some classes than others?</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[28]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">### Data exploration visualization code goes here.</span>
<span class="c1">### Feel free to use as many code cells as needed.</span>
<span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>
<span class="kn">import</span> <span class="nn">random</span>
<span class="c1"># Visualizations will be shown in the notebook.</span>
<span class="o">%</span><span class="k">matplotlib</span> inline

<span class="n">index</span> <span class="o">=</span> <span class="n">random</span><span class="o">.</span><span class="n">randint</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">X_train</span><span class="p">))</span>
<span class="n">image</span> <span class="o">=</span> <span class="n">X_train</span><span class="p">[</span><span class="n">index</span><span class="p">]</span><span class="o">.</span><span class="n">squeeze</span><span class="p">()</span>

<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Label of random image : &quot;</span><span class="p">,</span> <span class="n">y_train</span><span class="p">[</span><span class="n">index</span><span class="p">])</span>

<span class="n">plt</span><span class="o">.</span><span class="n">figure</span><span class="p">(</span><span class="n">figsize</span> <span class="o">=</span> <span class="p">(</span><span class="mi">2</span><span class="p">,</span><span class="mi">2</span><span class="p">))</span>
<span class="n">plt</span><span class="o">.</span><span class="n">imshow</span><span class="p">(</span><span class="n">image</span><span class="p">,</span> <span class="n">cmap</span><span class="o">=</span><span class="s1">&#39;gray&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>

<span class="c1">#print (&quot;----------------&quot;)</span>
<span class="n">sign_count_train</span> <span class="o">=</span> <span class="p">[]</span>
<span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">n_classes</span><span class="p">):</span>
    <span class="n">sign_count_train</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
<span class="c1">#print (sign_count)</span>
<span class="k">for</span> <span class="n">label</span> <span class="ow">in</span> <span class="n">y_train</span><span class="p">:</span>
    <span class="n">sign_count_train</span><span class="p">[</span><span class="n">label</span><span class="p">]</span> <span class="o">+=</span> <span class="mi">1</span>
<span class="n">plt</span><span class="o">.</span><span class="n">bar</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">arange</span><span class="p">(</span><span class="n">n_classes</span><span class="p">),</span> <span class="n">sign_count_train</span><span class="p">,</span> <span class="n">align</span><span class="o">=</span><span class="s1">&#39;center&#39;</span><span class="p">,</span> <span class="n">alpha</span><span class="o">=</span><span class="mf">0.6</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">xticks</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">n_classes</span><span class="p">,</span> <span class="mi">5</span><span class="p">))</span>
<span class="n">plt</span><span class="o">.</span><span class="n">xlabel</span><span class="p">(</span><span class="s1">&#39;Class(Label)&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">ylabel</span><span class="p">(</span><span class="s1">&#39;Count&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s1">&#39;Distribution of classes in training set&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>

<span class="n">sign_count_valid</span> <span class="o">=</span> <span class="p">[]</span>
<span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">n_classes</span><span class="p">):</span>
    <span class="n">sign_count_valid</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
<span class="c1">#print (sign_count)</span>
<span class="k">for</span> <span class="n">label</span> <span class="ow">in</span> <span class="n">y_valid</span><span class="p">:</span>
    <span class="n">sign_count_valid</span><span class="p">[</span><span class="n">label</span><span class="p">]</span> <span class="o">+=</span> <span class="mi">1</span>
<span class="n">plt</span><span class="o">.</span><span class="n">bar</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">arange</span><span class="p">(</span><span class="n">n_classes</span><span class="p">),</span> <span class="n">sign_count_valid</span><span class="p">,</span> <span class="n">align</span><span class="o">=</span><span class="s1">&#39;center&#39;</span><span class="p">,</span> <span class="n">alpha</span><span class="o">=</span><span class="mf">0.6</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">xticks</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">n_classes</span><span class="p">,</span> <span class="mi">5</span><span class="p">))</span>
<span class="n">plt</span><span class="o">.</span><span class="n">xlabel</span><span class="p">(</span><span class="s1">&#39;Class(Label)&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">ylabel</span><span class="p">(</span><span class="s1">&#39;Count&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s1">&#39;Distribution of classes in validation set&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>

<span class="n">sign_count_test</span> <span class="o">=</span> <span class="p">[]</span>
<span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">n_classes</span><span class="p">):</span>
    <span class="n">sign_count_test</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
<span class="c1">#print (sign_count)</span>
<span class="k">for</span> <span class="n">label</span> <span class="ow">in</span> <span class="n">y_test</span><span class="p">:</span>
    <span class="n">sign_count_test</span><span class="p">[</span><span class="n">label</span><span class="p">]</span> <span class="o">+=</span> <span class="mi">1</span>
<span class="n">plt</span><span class="o">.</span><span class="n">bar</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">arange</span><span class="p">(</span><span class="n">n_classes</span><span class="p">),</span> <span class="n">sign_count_test</span><span class="p">,</span> <span class="n">align</span><span class="o">=</span><span class="s1">&#39;center&#39;</span><span class="p">,</span> <span class="n">alpha</span><span class="o">=</span><span class="mf">0.6</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">xticks</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">n_classes</span><span class="p">,</span> <span class="mi">5</span><span class="p">))</span>
<span class="n">plt</span><span class="o">.</span><span class="n">xlabel</span><span class="p">(</span><span class="s1">&#39;Class(Label)&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">ylabel</span><span class="p">(</span><span class="s1">&#39;Count&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s1">&#39;Distribution of classes in test set&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Label of random image :  12
</pre>
</div>
</div>

<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<hr>
<h2 id="Step-2:-Design-and-Test-a-Model-Architecture">Step 2: Design and Test a Model Architecture<a class="anchor-link" href="#Step-2:-Design-and-Test-a-Model-Architecture">&#182;</a></h2><p>Design and implement a deep learning model that learns to recognize traffic signs. Train and test your model on the <a href="http://benchmark.ini.rub.de/?section=gtsrb&amp;subsection=dataset">German Traffic Sign Dataset</a>.</p>
<p>The LeNet-5 implementation shown in the <a href="https://classroom.udacity.com/nanodegrees/nd013/parts/fbf77062-5703-404e-b60c-95b78b2f3f9e/modules/6df7ae49-c61c-4bb2-a23e-6527e69209ec/lessons/601ae704-1035-4287-8b11-e2c2716217ad/concepts/d4aca031-508f-4e0b-b493-e7b706120f81">classroom</a> at the end of the CNN lesson is a solid starting point. You'll have to change the number of classes and possibly the preprocessing, but aside from that it's plug and play!</p>
<p>With the LeNet-5 solution from the lecture, you should expect a validation set accuracy of about 0.89. To meet specifications, the validation set accuracy will need to be at least 0.93. It is possible to get an even higher accuracy, but 0.93 is the minimum for a successful project submission.</p>
<p>There are various aspects to consider when thinking about this problem:</p>
<ul>
<li>Neural network architecture (is the network over or underfitting?)</li>
<li>Play around preprocessing techniques (normalization, rgb to grayscale, etc)</li>
<li>Number of examples per label (some have more than others).</li>
<li>Generate fake data.</li>
</ul>
<p>Here is an example of a <a href="http://yann.lecun.com/exdb/publis/pdf/sermanet-ijcnn-11.pdf">published baseline model on this problem</a>. It's not required to be familiar with the approach used in the paper but, it's good practice to try to read papers like these.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Pre-process-the-Data-Set-(normalization,-grayscale,-etc.)">Pre-process the Data Set (normalization, grayscale, etc.)<a class="anchor-link" href="#Pre-process-the-Data-Set-(normalization,-grayscale,-etc.)">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Minimally, the image data should be normalized so that the data has mean zero and equal variance. For image data, <code>(pixel - 128)/ 128</code> is a quick way to approximately normalize the data and can be used in this project.</p>
<p>Other pre-processing steps are optional. You can try different techniques to see if it improves performance.</p>
<p>Use the code cell (or multiple code cells, if necessary) to implement the first step of your project.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[29]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">### Preprocess the data here. It is required to normalize the data. Other preprocessing steps could include </span>
<span class="c1">### converting to grayscale, etc.</span>
<span class="c1">### Feel free to use as many code cells as needed.</span>
<span class="k">def</span> <span class="nf">rgb2gray</span><span class="p">(</span><span class="n">rgb</span><span class="p">):</span>
    <span class="n">rgb</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">=</span> <span class="n">rgb</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">*</span> <span class="mf">0.299</span>
    <span class="n">rgb</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="o">=</span> <span class="n">rgb</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="o">*</span> <span class="mf">0.587</span>
    <span class="n">rgb</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span> <span class="o">=</span> <span class="n">rgb</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span> <span class="o">*</span> <span class="mf">0.114</span>
    <span class="k">return</span> <span class="n">np</span><span class="o">.</span><span class="n">sum</span><span class="p">(</span><span class="n">rgb</span><span class="p">,</span> <span class="n">axis</span><span class="o">=</span><span class="mi">3</span><span class="p">,</span> <span class="n">keepdims</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>

<span class="n">image</span> <span class="o">=</span> <span class="n">X_train</span><span class="p">[</span><span class="n">index</span><span class="p">]</span><span class="o">.</span><span class="n">squeeze</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Before normalizing and converting to grayscale&quot;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">figure</span><span class="p">(</span><span class="n">figsize</span> <span class="o">=</span> <span class="p">(</span><span class="mi">2</span><span class="p">,</span><span class="mi">2</span><span class="p">))</span>
<span class="n">plt</span><span class="o">.</span><span class="n">imshow</span><span class="p">(</span><span class="n">image</span><span class="p">,</span> <span class="n">cmap</span><span class="o">=</span><span class="s1">&#39;gray&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>

<span class="n">X_train</span> <span class="o">=</span> <span class="p">(</span><span class="n">X_train</span> <span class="o">-</span> <span class="mf">128.0</span><span class="p">)</span> <span class="o">/</span> <span class="mf">128.0</span>
<span class="n">X_train</span> <span class="o">=</span> <span class="n">rgb2gray</span><span class="p">(</span><span class="n">X_train</span><span class="p">)</span>
<span class="n">X_valid</span> <span class="o">=</span> <span class="p">(</span><span class="n">X_valid</span> <span class="o">-</span> <span class="mf">128.0</span><span class="p">)</span> <span class="o">/</span> <span class="mf">128.0</span>
<span class="n">X_valid</span> <span class="o">=</span> <span class="n">rgb2gray</span><span class="p">(</span><span class="n">X_valid</span><span class="p">)</span>
<span class="n">X_test</span>  <span class="o">=</span> <span class="p">(</span><span class="n">X_test</span> <span class="o">-</span> <span class="mf">128.0</span><span class="p">)</span> <span class="o">/</span> <span class="mf">128.0</span>
<span class="n">X_test</span>  <span class="o">=</span> <span class="n">rgb2gray</span><span class="p">(</span><span class="n">X_test</span><span class="p">)</span>

<span class="n">image</span> <span class="o">=</span> <span class="n">X_train</span><span class="p">[</span><span class="n">index</span><span class="p">]</span><span class="o">.</span><span class="n">squeeze</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;After normalizing and converting to grayscale&quot;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">figure</span><span class="p">(</span><span class="n">figsize</span> <span class="o">=</span> <span class="p">(</span><span class="mi">2</span><span class="p">,</span><span class="mi">2</span><span class="p">))</span>
<span class="n">plt</span><span class="o">.</span><span class="n">imshow</span><span class="p">(</span><span class="n">image</span><span class="p">,</span> <span class="n">cmap</span><span class="o">=</span><span class="s1">&#39;gray&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>

<span class="nb">print</span> <span class="p">(</span><span class="n">X_train</span><span class="p">[</span><span class="n">index</span><span class="p">]</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Before normalizing and converting to grayscale
</pre>
</div>
</div>

<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

<div class="output_area">

<div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>After normalizing and converting to grayscale
</pre>
</div>
</div>

<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

<div class="output_area">

<div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>(32, 32, 1)
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Model-Architecture">Model Architecture<a class="anchor-link" href="#Model-Architecture">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[30]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">### Define your architecture here.</span>
<span class="c1">### Feel free to use as many code cells as needed.</span>
<span class="kn">from</span> <span class="nn">tensorflow.contrib.layers</span> <span class="k">import</span> <span class="n">flatten</span>

<span class="k">def</span> <span class="nf">TSC_model</span><span class="p">(</span><span class="n">x</span><span class="p">):</span>
    <span class="n">mu</span> <span class="o">=</span> <span class="mf">0.0</span>
    <span class="n">sigma</span> <span class="o">=</span> <span class="mf">0.1</span>
    <span class="c1">#dropout = 0.8</span>
    
    <span class="c1"># Layer 1: Convolutional. Input = 32x32x1. Output = 28x28x6.</span>
    <span class="n">conv1_W</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">Variable</span><span class="p">(</span><span class="n">tf</span><span class="o">.</span><span class="n">truncated_normal</span><span class="p">(</span><span class="n">shape</span><span class="o">=</span><span class="p">(</span><span class="mi">5</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">6</span><span class="p">),</span> <span class="n">mean</span> <span class="o">=</span> <span class="n">mu</span><span class="p">,</span> <span class="n">stddev</span> <span class="o">=</span> <span class="n">sigma</span><span class="p">))</span>
    <span class="n">conv1_b</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">Variable</span><span class="p">(</span><span class="n">tf</span><span class="o">.</span><span class="n">zeros</span><span class="p">(</span><span class="mi">6</span><span class="p">))</span>
    <span class="n">conv1</span>   <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">nn</span><span class="o">.</span><span class="n">conv2d</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">conv1_W</span><span class="p">,</span> <span class="n">strides</span><span class="o">=</span><span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">],</span> <span class="n">padding</span><span class="o">=</span><span class="s1">&#39;VALID&#39;</span><span class="p">)</span> <span class="o">+</span> <span class="n">conv1_b</span>

    <span class="c1"># Activation.</span>
    <span class="n">conv1</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">nn</span><span class="o">.</span><span class="n">relu</span><span class="p">(</span><span class="n">conv1</span><span class="p">)</span>
    <span class="c1">#conv1 = tf.nn.dropout(conv1, dropout)</span>

    <span class="c1"># Pooling. Input = 28x28x6. Output = 14x14x6.</span>
    <span class="n">conv1</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">nn</span><span class="o">.</span><span class="n">max_pool</span><span class="p">(</span><span class="n">conv1</span><span class="p">,</span> <span class="n">ksize</span><span class="o">=</span><span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">1</span><span class="p">],</span> <span class="n">strides</span><span class="o">=</span><span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">1</span><span class="p">],</span> <span class="n">padding</span><span class="o">=</span><span class="s1">&#39;SAME&#39;</span><span class="p">)</span>
    <span class="c1">#conv1 = tf.nn.dropout(conv1, dropout)</span>

    <span class="c1"># Layer 2: Convolutional. Output = 10x10x16.</span>
    <span class="n">conv2_W</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">Variable</span><span class="p">(</span><span class="n">tf</span><span class="o">.</span><span class="n">truncated_normal</span><span class="p">(</span><span class="n">shape</span><span class="o">=</span><span class="p">(</span><span class="mi">5</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="mi">6</span><span class="p">,</span> <span class="mi">16</span><span class="p">),</span> <span class="n">mean</span> <span class="o">=</span> <span class="n">mu</span><span class="p">,</span> <span class="n">stddev</span> <span class="o">=</span> <span class="n">sigma</span><span class="p">))</span>
    <span class="n">conv2_b</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">Variable</span><span class="p">(</span><span class="n">tf</span><span class="o">.</span><span class="n">zeros</span><span class="p">(</span><span class="mi">16</span><span class="p">))</span>
    <span class="n">conv2</span>   <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">nn</span><span class="o">.</span><span class="n">conv2d</span><span class="p">(</span><span class="n">conv1</span><span class="p">,</span> <span class="n">conv2_W</span><span class="p">,</span> <span class="n">strides</span><span class="o">=</span><span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">],</span> <span class="n">padding</span><span class="o">=</span><span class="s1">&#39;VALID&#39;</span><span class="p">)</span> <span class="o">+</span> <span class="n">conv2_b</span>
    
    <span class="c1"># Activation.</span>
    <span class="n">conv2</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">nn</span><span class="o">.</span><span class="n">relu</span><span class="p">(</span><span class="n">conv2</span><span class="p">)</span>
    <span class="c1">#conv2 = tf.nn.dropout(conv2, dropout)</span>

    <span class="c1"># Pooling. Input = 10x10x16. Output = 5x5x16.</span>
    <span class="n">conv2</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">nn</span><span class="o">.</span><span class="n">max_pool</span><span class="p">(</span><span class="n">conv2</span><span class="p">,</span> <span class="n">ksize</span><span class="o">=</span><span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">1</span><span class="p">],</span> <span class="n">strides</span><span class="o">=</span><span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">1</span><span class="p">],</span> <span class="n">padding</span><span class="o">=</span><span class="s1">&#39;SAME&#39;</span><span class="p">)</span>
    <span class="c1">#conv2 = tf.nn.dropout(conv2, dropout)</span>

    <span class="c1"># Flatten. Input = 5x5x16. Output = 400.</span>
    <span class="n">fc0</span>   <span class="o">=</span> <span class="n">flatten</span><span class="p">(</span><span class="n">conv2</span><span class="p">)</span>
    
    <span class="c1"># Layer 3: Fully Connected. Input = 400. Output = 120.</span>
    <span class="n">fc1_W</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">Variable</span><span class="p">(</span><span class="n">tf</span><span class="o">.</span><span class="n">truncated_normal</span><span class="p">(</span><span class="n">shape</span><span class="o">=</span><span class="p">(</span><span class="mi">400</span><span class="p">,</span> <span class="mi">120</span><span class="p">),</span> <span class="n">mean</span> <span class="o">=</span> <span class="n">mu</span><span class="p">,</span> <span class="n">stddev</span> <span class="o">=</span> <span class="n">sigma</span><span class="p">))</span>
    <span class="n">fc1_b</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">Variable</span><span class="p">(</span><span class="n">tf</span><span class="o">.</span><span class="n">zeros</span><span class="p">(</span><span class="mi">120</span><span class="p">))</span>
    <span class="n">fc1</span>   <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">matmul</span><span class="p">(</span><span class="n">fc0</span><span class="p">,</span> <span class="n">fc1_W</span><span class="p">)</span> <span class="o">+</span> <span class="n">fc1_b</span>
    
    <span class="c1"># Activation.</span>
    <span class="n">fc1</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">nn</span><span class="o">.</span><span class="n">relu</span><span class="p">(</span><span class="n">fc1</span><span class="p">)</span>
    <span class="c1">#fc1 = tf.nn.dropout(tf.nn.relu(fc1), dropout)</span>

    <span class="c1"># Layer 4: Fully Connected. Input = 120. Output = 84.</span>
    <span class="n">fc2_W</span>  <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">Variable</span><span class="p">(</span><span class="n">tf</span><span class="o">.</span><span class="n">truncated_normal</span><span class="p">(</span><span class="n">shape</span><span class="o">=</span><span class="p">(</span><span class="mi">120</span><span class="p">,</span> <span class="mi">84</span><span class="p">),</span> <span class="n">mean</span> <span class="o">=</span> <span class="n">mu</span><span class="p">,</span> <span class="n">stddev</span> <span class="o">=</span> <span class="n">sigma</span><span class="p">))</span>
    <span class="n">fc2_b</span>  <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">Variable</span><span class="p">(</span><span class="n">tf</span><span class="o">.</span><span class="n">zeros</span><span class="p">(</span><span class="mi">84</span><span class="p">))</span>
    <span class="n">fc2</span>    <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">matmul</span><span class="p">(</span><span class="n">fc1</span><span class="p">,</span> <span class="n">fc2_W</span><span class="p">)</span> <span class="o">+</span> <span class="n">fc2_b</span>
    
    <span class="c1"># Activation.</span>
    <span class="n">fc2</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">nn</span><span class="o">.</span><span class="n">relu</span><span class="p">(</span><span class="n">fc2</span><span class="p">)</span>
    <span class="c1">#fc2 = tf.nn.dropout(tf.nn.relu(fc2), dropout)</span>

    <span class="c1"># Layer 5: Fully Connected. Input = 84. Output = 43.</span>
    <span class="n">fc3_W</span>  <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">Variable</span><span class="p">(</span><span class="n">tf</span><span class="o">.</span><span class="n">truncated_normal</span><span class="p">(</span><span class="n">shape</span><span class="o">=</span><span class="p">(</span><span class="mi">84</span><span class="p">,</span> <span class="mi">43</span><span class="p">),</span> <span class="n">mean</span> <span class="o">=</span> <span class="n">mu</span><span class="p">,</span> <span class="n">stddev</span> <span class="o">=</span> <span class="n">sigma</span><span class="p">))</span>
    <span class="n">fc3_b</span>  <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">Variable</span><span class="p">(</span><span class="n">tf</span><span class="o">.</span><span class="n">zeros</span><span class="p">(</span><span class="mi">43</span><span class="p">))</span>
    <span class="n">logits</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">matmul</span><span class="p">(</span><span class="n">fc2</span><span class="p">,</span> <span class="n">fc3_W</span><span class="p">)</span> <span class="o">+</span> <span class="n">fc3_b</span>
    
    <span class="k">return</span> <span class="n">logits</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Train,-Validate-and-Test-the-Model">Train, Validate and Test the Model<a class="anchor-link" href="#Train,-Validate-and-Test-the-Model">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>A validation set can be used to assess how well the model is performing. A low accuracy on the training and validation
sets imply underfitting. A high accuracy on the training set but low accuracy on the validation set implies overfitting.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[31]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">### Train your model here.</span>
<span class="c1">### Calculate and report the accuracy on the training and validation set.</span>
<span class="c1">### Once a final model architecture is selected, </span>
<span class="c1">### the accuracy on the test set should be calculated and reported as well.</span>
<span class="c1">### Feel free to use as many code cells as needed.</span>
<span class="kn">from</span> <span class="nn">sklearn.utils</span> <span class="k">import</span> <span class="n">shuffle</span>

<span class="c1"># Hyperparameters</span>
<span class="n">EPOCHS</span> <span class="o">=</span> <span class="mi">20</span>
<span class="n">BATCH_SIZE</span> <span class="o">=</span> <span class="mi">128</span>
<span class="n">rate</span> <span class="o">=</span> <span class="mf">0.001</span>

<span class="n">x</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">placeholder</span><span class="p">(</span><span class="n">tf</span><span class="o">.</span><span class="n">float32</span><span class="p">,</span> <span class="p">(</span><span class="kc">None</span><span class="p">,</span> <span class="mi">32</span><span class="p">,</span> <span class="mi">32</span><span class="p">,</span> <span class="mi">1</span><span class="p">))</span>
<span class="n">y</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">placeholder</span><span class="p">(</span><span class="n">tf</span><span class="o">.</span><span class="n">int32</span><span class="p">,</span> <span class="p">(</span><span class="kc">None</span><span class="p">))</span>
<span class="n">one_hot_y</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">one_hot</span><span class="p">(</span><span class="n">y</span><span class="p">,</span> <span class="mi">43</span><span class="p">)</span>
<span class="n">keep_prob</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">placeholder</span><span class="p">(</span><span class="n">tf</span><span class="o">.</span><span class="n">float32</span><span class="p">)</span>

<span class="n">logits</span> <span class="o">=</span> <span class="n">TSC_model</span><span class="p">(</span><span class="n">x</span><span class="p">)</span>
<span class="n">cross_entropy</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">nn</span><span class="o">.</span><span class="n">softmax_cross_entropy_with_logits</span><span class="p">(</span><span class="n">logits</span><span class="o">=</span><span class="n">logits</span><span class="p">,</span> <span class="n">labels</span><span class="o">=</span><span class="n">one_hot_y</span><span class="p">)</span>
<span class="n">loss_operation</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">reduce_mean</span><span class="p">(</span><span class="n">cross_entropy</span><span class="p">)</span>
<span class="n">optimizer</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">train</span><span class="o">.</span><span class="n">AdamOptimizer</span><span class="p">(</span><span class="n">learning_rate</span> <span class="o">=</span> <span class="n">rate</span><span class="p">)</span>
<span class="n">training_operation</span> <span class="o">=</span> <span class="n">optimizer</span><span class="o">.</span><span class="n">minimize</span><span class="p">(</span><span class="n">loss_operation</span><span class="p">)</span>

<span class="n">correct_prediction</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">equal</span><span class="p">(</span><span class="n">tf</span><span class="o">.</span><span class="n">argmax</span><span class="p">(</span><span class="n">logits</span><span class="p">,</span> <span class="mi">1</span><span class="p">),</span> <span class="n">tf</span><span class="o">.</span><span class="n">argmax</span><span class="p">(</span><span class="n">one_hot_y</span><span class="p">,</span> <span class="mi">1</span><span class="p">))</span>
<span class="n">accuracy_operation</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">reduce_mean</span><span class="p">(</span><span class="n">tf</span><span class="o">.</span><span class="n">cast</span><span class="p">(</span><span class="n">correct_prediction</span><span class="p">,</span> <span class="n">tf</span><span class="o">.</span><span class="n">float32</span><span class="p">))</span>
<span class="n">saver</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">train</span><span class="o">.</span><span class="n">Saver</span><span class="p">()</span>

<span class="k">def</span> <span class="nf">evaluate</span><span class="p">(</span><span class="n">X_data</span><span class="p">,</span> <span class="n">y_data</span><span class="p">):</span>
    <span class="n">num_examples</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">X_data</span><span class="p">)</span>
    <span class="n">total_accuracy</span> <span class="o">=</span> <span class="mi">0</span>
    <span class="n">total_loss</span> <span class="o">=</span> <span class="mi">0</span>
    <span class="n">sess</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">get_default_session</span><span class="p">()</span>
    <span class="k">for</span> <span class="n">offset</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">num_examples</span><span class="p">,</span> <span class="n">BATCH_SIZE</span><span class="p">):</span>
        <span class="n">batch_x</span><span class="p">,</span> <span class="n">batch_y</span> <span class="o">=</span> <span class="n">X_data</span><span class="p">[</span><span class="n">offset</span><span class="p">:</span><span class="n">offset</span><span class="o">+</span><span class="n">BATCH_SIZE</span><span class="p">],</span> <span class="n">y_data</span><span class="p">[</span><span class="n">offset</span><span class="p">:</span><span class="n">offset</span><span class="o">+</span><span class="n">BATCH_SIZE</span><span class="p">]</span>
        <span class="n">loss</span><span class="p">,</span> <span class="n">accuracy</span> <span class="o">=</span> <span class="n">sess</span><span class="o">.</span><span class="n">run</span><span class="p">([</span><span class="n">loss_operation</span><span class="p">,</span> <span class="n">accuracy_operation</span><span class="p">],</span> <span class="n">feed_dict</span><span class="o">=</span><span class="p">{</span><span class="n">x</span><span class="p">:</span> <span class="n">batch_x</span><span class="p">,</span> <span class="n">y</span><span class="p">:</span> <span class="n">batch_y</span><span class="p">})</span>
        <span class="n">total_loss</span> <span class="o">+=</span> <span class="p">(</span><span class="n">loss</span> <span class="o">*</span> <span class="nb">len</span><span class="p">(</span><span class="n">batch_x</span><span class="p">))</span>
        <span class="n">total_accuracy</span> <span class="o">+=</span> <span class="p">(</span><span class="n">accuracy</span> <span class="o">*</span> <span class="nb">len</span><span class="p">(</span><span class="n">batch_x</span><span class="p">))</span>
    <span class="k">return</span> <span class="n">total_loss</span> <span class="o">/</span> <span class="n">num_examples</span><span class="p">,</span> <span class="n">total_accuracy</span> <span class="o">/</span> <span class="n">num_examples</span>

<span class="k">with</span> <span class="n">tf</span><span class="o">.</span><span class="n">Session</span><span class="p">()</span> <span class="k">as</span> <span class="n">sess</span><span class="p">:</span>
    <span class="n">sess</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">tf</span><span class="o">.</span><span class="n">global_variables_initializer</span><span class="p">())</span>
    <span class="n">num_examples</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">X_train</span><span class="p">)</span>
    
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Training...&quot;</span><span class="p">)</span>
    <span class="nb">print</span><span class="p">()</span>
    <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">EPOCHS</span><span class="p">):</span>
        <span class="n">X_train</span><span class="p">,</span> <span class="n">y_train</span> <span class="o">=</span> <span class="n">shuffle</span><span class="p">(</span><span class="n">X_train</span><span class="p">,</span> <span class="n">y_train</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">offset</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">num_examples</span><span class="p">,</span> <span class="n">BATCH_SIZE</span><span class="p">):</span>
            <span class="n">end</span> <span class="o">=</span> <span class="n">offset</span> <span class="o">+</span> <span class="n">BATCH_SIZE</span>
            <span class="n">batch_x</span><span class="p">,</span> <span class="n">batch_y</span> <span class="o">=</span> <span class="n">X_train</span><span class="p">[</span><span class="n">offset</span><span class="p">:</span><span class="n">end</span><span class="p">],</span> <span class="n">y_train</span><span class="p">[</span><span class="n">offset</span><span class="p">:</span><span class="n">end</span><span class="p">]</span>
            <span class="n">sess</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">training_operation</span><span class="p">,</span> <span class="n">feed_dict</span><span class="o">=</span><span class="p">{</span><span class="n">x</span><span class="p">:</span> <span class="n">batch_x</span><span class="p">,</span> <span class="n">y</span><span class="p">:</span> <span class="n">batch_y</span><span class="p">})</span>
        
        <span class="n">train_loss</span><span class="p">,</span> <span class="n">train_accuracy</span> <span class="o">=</span> <span class="n">evaluate</span><span class="p">(</span><span class="n">X_train</span><span class="p">,</span> <span class="n">y_train</span><span class="p">)</span>
        <span class="n">validation_loss</span><span class="p">,</span> <span class="n">validation_accuracy</span> <span class="o">=</span> <span class="n">evaluate</span><span class="p">(</span><span class="n">X_valid</span><span class="p">,</span> <span class="n">y_valid</span><span class="p">)</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;EPOCH </span><span class="si">{}</span><span class="s2"> ...&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">i</span> <span class="o">+</span> <span class="mi">1</span><span class="p">))</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Train loss = </span><span class="si">{:.3f}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">train_loss</span><span class="p">))</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Train Accuracy = </span><span class="si">{:.3f}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">train_accuracy</span><span class="p">))</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Validation loss = </span><span class="si">{:.3f}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">validation_loss</span><span class="p">))</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Validation Accuracy = </span><span class="si">{:.3f}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">validation_accuracy</span><span class="p">))</span>
        <span class="nb">print</span><span class="p">()</span>
    
    <span class="n">saver</span><span class="o">.</span><span class="n">save</span><span class="p">(</span><span class="n">sess</span><span class="p">,</span> <span class="s1">&#39;./traffic-signs-classifier&#39;</span><span class="p">)</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Model saved&quot;</span><span class="p">)</span>
    
<span class="k">with</span> <span class="n">tf</span><span class="o">.</span><span class="n">Session</span><span class="p">()</span> <span class="k">as</span> <span class="n">sess</span><span class="p">:</span>
    <span class="n">saver</span><span class="o">.</span><span class="n">restore</span><span class="p">(</span><span class="n">sess</span><span class="p">,</span> <span class="n">tf</span><span class="o">.</span><span class="n">train</span><span class="o">.</span><span class="n">latest_checkpoint</span><span class="p">(</span><span class="s1">&#39;.&#39;</span><span class="p">))</span>
    <span class="n">result</span> <span class="o">=</span> <span class="n">evaluate</span><span class="p">(</span><span class="n">X_valid</span><span class="p">,</span> <span class="n">y_valid</span><span class="p">)</span>
    <span class="n">result_test</span> <span class="o">=</span> <span class="n">evaluate</span><span class="p">(</span><span class="n">X_test</span><span class="p">,</span> <span class="n">y_test</span><span class="p">)</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Validation set accuracy = </span><span class="si">{:.3f}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">result</span><span class="p">[</span><span class="mi">1</span><span class="p">]))</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Test set accuracy = </span><span class="si">{:.3f}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">result_test</span><span class="p">[</span><span class="mi">1</span><span class="p">]))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Training...

EPOCH 1 ...
Train loss = 0.466
Train Accuracy = 0.875
Validation loss = 0.721
Validation Accuracy = 0.818

EPOCH 2 ...
Train loss = 0.277
Train Accuracy = 0.928
Validation loss = 0.569
Validation Accuracy = 0.835

EPOCH 3 ...
Train loss = 0.156
Train Accuracy = 0.964
Validation loss = 0.464
Validation Accuracy = 0.885

EPOCH 4 ...
Train loss = 0.098
Train Accuracy = 0.976
Validation loss = 0.372
Validation Accuracy = 0.903

EPOCH 5 ...
Train loss = 0.090
Train Accuracy = 0.977
Validation loss = 0.419
Validation Accuracy = 0.895

EPOCH 6 ...
Train loss = 0.067
Train Accuracy = 0.982
Validation loss = 0.387
Validation Accuracy = 0.906

EPOCH 7 ...
Train loss = 0.044
Train Accuracy = 0.990
Validation loss = 0.327
Validation Accuracy = 0.922

EPOCH 8 ...
Train loss = 0.035
Train Accuracy = 0.992
Validation loss = 0.431
Validation Accuracy = 0.908

EPOCH 9 ...
Train loss = 0.038
Train Accuracy = 0.990
Validation loss = 0.394
Validation Accuracy = 0.917

EPOCH 10 ...
Train loss = 0.032
Train Accuracy = 0.992
Validation loss = 0.354
Validation Accuracy = 0.915

EPOCH 11 ...
Train loss = 0.025
Train Accuracy = 0.994
Validation loss = 0.459
Validation Accuracy = 0.911

EPOCH 12 ...
Train loss = 0.017
Train Accuracy = 0.996
Validation loss = 0.403
Validation Accuracy = 0.921

EPOCH 13 ...
Train loss = 0.033
Train Accuracy = 0.990
Validation loss = 0.444
Validation Accuracy = 0.908

EPOCH 14 ...
Train loss = 0.039
Train Accuracy = 0.987
Validation loss = 0.460
Validation Accuracy = 0.912

EPOCH 15 ...
Train loss = 0.016
Train Accuracy = 0.996
Validation loss = 0.467
Validation Accuracy = 0.911

EPOCH 16 ...
Train loss = 0.008
Train Accuracy = 0.998
Validation loss = 0.341
Validation Accuracy = 0.935

EPOCH 17 ...
Train loss = 0.012
Train Accuracy = 0.997
Validation loss = 0.372
Validation Accuracy = 0.924

EPOCH 18 ...
Train loss = 0.024
Train Accuracy = 0.993
Validation loss = 0.495
Validation Accuracy = 0.914

EPOCH 19 ...
Train loss = 0.019
Train Accuracy = 0.995
Validation loss = 0.358
Validation Accuracy = 0.933

EPOCH 20 ...
Train loss = 0.006
Train Accuracy = 0.999
Validation loss = 0.323
Validation Accuracy = 0.939

Model saved
INFO:tensorflow:Restoring parameters from ./traffic-signs-classifier
Validation set accuracy = 0.939
Test set accuracy = 0.915
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<hr>
<h2 id="Step-3:-Test-a-Model-on-New-Images">Step 3: Test a Model on New Images<a class="anchor-link" href="#Step-3:-Test-a-Model-on-New-Images">&#182;</a></h2><p>To give yourself more insight into how your model is working, download at least five pictures of German traffic signs from the web and use your model to predict the traffic sign type.</p>
<p>You may find <code>signnames.csv</code> useful as it contains mappings from the class id (integer) to the actual sign name.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Load-and-Output-the-Images">Load and Output the Images<a class="anchor-link" href="#Load-and-Output-the-Images">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[32]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">### Load the images and plot them here.</span>
<span class="c1">### Feel free to use as many code cells as needed.</span>
<span class="kn">import</span> <span class="nn">csv</span>
<span class="kn">import</span> <span class="nn">cv2</span>

<span class="n">sign_detail</span> <span class="o">=</span> <span class="p">[]</span>
<span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="s1">&#39;signnames.csv&#39;</span><span class="p">,</span> <span class="s1">&#39;r&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
    <span class="k">for</span> <span class="n">entire_line</span> <span class="ow">in</span> <span class="n">f</span><span class="o">.</span><span class="n">readlines</span><span class="p">()[</span><span class="mi">1</span><span class="p">:]:</span>
        <span class="n">detail</span> <span class="o">=</span> <span class="n">entire_line</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s1">&#39;,&#39;</span><span class="p">)</span>
        <span class="n">sign_detail</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">detail</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span>
        
<span class="c1">#print (sign_detail)</span>
<span class="c1">#print (len(sign_detail))</span>

<span class="n">imagefile</span> <span class="o">=</span> <span class="p">[{</span><span class="s1">&#39;Image&#39;</span><span class="p">:</span> <span class="s1">&#39;TestImage/001.jpg&#39;</span><span class="p">,</span> <span class="s1">&#39;Label&#39;</span> <span class="p">:</span> <span class="mi">13</span><span class="p">},</span>\
             <span class="p">{</span><span class="s1">&#39;Image&#39;</span><span class="p">:</span> <span class="s1">&#39;TestImage/002.jpg&#39;</span><span class="p">,</span> <span class="s1">&#39;Label&#39;</span> <span class="p">:</span> <span class="mi">14</span><span class="p">},</span>\
             <span class="p">{</span><span class="s1">&#39;Image&#39;</span><span class="p">:</span> <span class="s1">&#39;TestImage/003.jpg&#39;</span><span class="p">,</span> <span class="s1">&#39;Label&#39;</span> <span class="p">:</span> <span class="mi">11</span><span class="p">},</span>\
             <span class="p">{</span><span class="s1">&#39;Image&#39;</span><span class="p">:</span> <span class="s1">&#39;TestImage/004.jpg&#39;</span><span class="p">,</span> <span class="s1">&#39;Label&#39;</span> <span class="p">:</span> <span class="mi">20</span><span class="p">},</span>\
             <span class="p">{</span><span class="s1">&#39;Image&#39;</span><span class="p">:</span> <span class="s1">&#39;TestImage/005.jpg&#39;</span><span class="p">,</span> <span class="s1">&#39;Label&#39;</span> <span class="p">:</span> <span class="mi">27</span><span class="p">}]</span>

<span class="n">process_image</span> <span class="o">=</span> <span class="p">[]</span>

<span class="k">for</span> <span class="n">img</span> <span class="ow">in</span> <span class="n">imagefile</span><span class="p">:</span>
    <span class="n">image</span> <span class="o">=</span> <span class="n">cv2</span><span class="o">.</span><span class="n">resize</span><span class="p">(</span><span class="n">plt</span><span class="o">.</span><span class="n">imread</span><span class="p">(</span><span class="n">img</span><span class="p">[</span><span class="s1">&#39;Image&#39;</span><span class="p">]),(</span><span class="mi">32</span><span class="p">,</span><span class="mi">32</span><span class="p">))</span>
    <span class="n">process_image</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">image</span><span class="p">)</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">figure</span><span class="p">(</span><span class="n">figsize</span> <span class="o">=</span> <span class="p">(</span><span class="mi">2</span><span class="p">,</span><span class="mi">2</span><span class="p">))</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="n">sign_detail</span><span class="p">[</span><span class="n">img</span><span class="p">[</span><span class="s1">&#39;Label&#39;</span><span class="p">]])</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">imshow</span><span class="p">(</span><span class="n">image</span><span class="p">)</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Predict-the-Sign-Type-for-Each-Image">Predict the Sign Type for Each Image<a class="anchor-link" href="#Predict-the-Sign-Type-for-Each-Image">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[40]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">### Run the predictions here and use the model to output the prediction for each image.</span>
<span class="c1">### Make sure to pre-process the images with the same pre-processing pipeline used earlier.</span>
<span class="c1">### Feel free to use as many code cells as needed.</span>
<span class="k">for</span> <span class="n">img</span> <span class="ow">in</span> <span class="n">process_image</span><span class="p">:</span>
    <span class="n">img</span> <span class="o">=</span> <span class="p">(</span><span class="n">img</span> <span class="o">-</span> <span class="mf">128.0</span><span class="p">)</span> <span class="o">/</span> <span class="mf">128.0</span>
<span class="n">process_image</span> <span class="o">=</span> <span class="n">rgb2gray</span><span class="p">(</span><span class="n">process_image</span><span class="p">)</span>
<span class="n">image</span> <span class="o">=</span> <span class="n">process_image</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">squeeze</span><span class="p">()</span>
<span class="n">plt</span><span class="o">.</span><span class="n">figure</span><span class="p">(</span><span class="n">figsize</span> <span class="o">=</span> <span class="p">(</span><span class="mi">2</span><span class="p">,</span><span class="mi">2</span><span class="p">))</span>
<span class="n">plt</span><span class="o">.</span><span class="n">imshow</span><span class="p">(</span><span class="n">image</span><span class="p">,</span> <span class="n">cmap</span><span class="o">=</span><span class="s1">&#39;gray&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>

<span class="k">with</span> <span class="n">tf</span><span class="o">.</span><span class="n">Session</span><span class="p">()</span> <span class="k">as</span> <span class="n">sess</span><span class="p">:</span>
    <span class="n">saver</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">train</span><span class="o">.</span><span class="n">Saver</span><span class="p">()</span>
    <span class="n">saver</span><span class="o">.</span><span class="n">restore</span><span class="p">(</span><span class="n">sess</span><span class="p">,</span> <span class="n">tf</span><span class="o">.</span><span class="n">train</span><span class="o">.</span><span class="n">latest_checkpoint</span><span class="p">(</span><span class="s1">&#39;.&#39;</span><span class="p">))</span>
    <span class="n">out</span> <span class="o">=</span> <span class="n">sess</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">tf</span><span class="o">.</span><span class="n">nn</span><span class="o">.</span><span class="n">top_k</span><span class="p">(</span><span class="n">tf</span><span class="o">.</span><span class="n">nn</span><span class="o">.</span><span class="n">softmax</span><span class="p">(</span><span class="n">logits</span><span class="p">),</span> <span class="n">k</span><span class="o">=</span><span class="mi">5</span><span class="p">),</span> <span class="n">feed_dict</span> <span class="o">=</span> <span class="p">{</span><span class="n">x</span><span class="p">:</span> <span class="n">process_image</span><span class="p">})</span>
<span class="nb">print</span> <span class="p">(</span><span class="n">out</span><span class="p">)</span>

<span class="nb">print</span> <span class="p">(</span><span class="s2">&quot;</span><span class="se">\n</span><span class="s2">        [Prediction]&quot;</span><span class="p">)</span>
<span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">out</span><span class="p">[</span><span class="mi">1</span><span class="p">])):</span>
    <span class="nb">print</span> <span class="p">(</span><span class="s2">&quot;Sign </span><span class="si">{}</span><span class="s2">:&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">i</span><span class="o">+</span><span class="mi">1</span><span class="p">),</span> <span class="n">sign_detail</span><span class="p">[</span><span class="n">out</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="n">i</span><span class="p">][</span><span class="mi">0</span><span class="p">]])</span>
    <span class="nb">print</span> <span class="p">()</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAI8AAACPCAYAAADDY4iTAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAIABJREFUeJztfVuMJNd53nf6fp/uuc/srkitCcgkIWEdSKQEEpKNJIYQBFASwAbtwHAuMPRgJQEUIHacB8VBHuSAEZAYshErimELcZzYgpgEiizJiI1AK1lRLDJkpBUvonbF3Z3ZmemZvt+nTh56vjN/nTlVXV0zO7s05gcK3V1ddepUna/++/mP0lrjgi4oDiUedAcu6O1LF+C5oNh0AZ4Lik0X4Lmg2HQBnguKTRfguaDYdCrwKKU+rJT6nlLqNaXUL51Vpy7o7UEqrp9HKZUA8BqAvwzgLoBvAXhOa/29s+veBT3MdBrO8xSA17XWt7TWYwC/D+AjZ9OtC3o7UOoU514C8Jb4fRtTQPlIKXXhwn6bk9ZaufafBjyR6fnnn8eXvvQlfPCDH8RwOPRtg8EAnudBKWU2AObT8zyMx2NMJhO88sorePzxx027iUQCiUQCyWQSyWQSnufh8PAQnufB8zwAgNYaFM38/uqrr+Jd73rX8UNIpcyWTqeRTqeRyWSQyWSQzWbNVigUsLCwgGq1ihdeeAEf/ehHzTnJZBKHh4eYTCY4PDz03UMikUAqlUIymUQqlUIiMWX4n/70p/Gxj30Mk8kEk8kE4/EY4/HY93wajQYODg7QaDQwGAx8z5X3c/36dTz11FMYDAYYDAbo9/tQSiGRSEAphWw2i3K5jHK5jEqlYu41mUwCAAaDAb74xS/i2WefRb/fN20Mh0N87nOfCxzX04DnDoB3iN+Xj/adoBdeeAE3b95Et9vFxsYG1tfXMRqNDCi01idAIx8OAWGT3Od5njme39mGbCuIJHgJykQigXQ6jXw+j2KxiGKxiEqlglKphEwmg3w+bwYhkUhgMpmYNnhPdpvy/mS/2OfDw0MDwvF4DK216QNfEB7PTSmFZDKJdDptngmBmkqlkMlkUCgUkM/nzcvB/9mfdDqNYrGIW7du4fXXXzdjE0anAc+3ADymlHoEwBaA5wD8jOvAJ598Er1eD08++SQ8z0Ov1zNv6OHhoe9B84HKB2tzD0mSy0hygUe2GURysJPJpAFJqVRCuVxGqVRCsVj0DShBIcHhAg+PlX2UwOF3CR5gyhkJVD4zuSmlkEqlzH0RSOSekoMSPAQW+5dKpVAoFPDEE0/gkUceQbfbxWAwwIsvvhj4rGKDR2t9qJT6GICvYKp4f1ZrfcN1bLPZxMLCAjqdjnlo8g2Sg2b/L2l5ednuwwkw2G82j5OfS0tLJ7id3PhWptNpZLNZw3kInkKhgGeeeQa5XM4Ag0Qwz+I8nufhfe97n+85kMMSFOQq6XTacEGKOLldvXrViCCKyGw2i1wuh1wuh0wm4+NEcmN/nnzySWSzWRweHhrxSfEbRKfSebTWfwTgXbOO8zwPKysrJ/QQOehB3yURPGGcI+g/ud8GoQRNOp1GLpdDsVhEoVBAsVhEPp83A0AAPP300wYgbNv1QthcicdrrfHe977Xp+tIUUFxY3MbHjMej02bjz32GA4PD41Y8zwPuVzOAIjg4/XZ1mg0gtYak8kEV65cQa/Xw2Aw8KkTYXQuCrOLi7gAZP/H73Ep6rlSrBA8hUIBlUrFBx4qu7bocd2Tzcnkb4pqW78ZjUYGPMlkEtls1qfbHB4eIpVKYTwe+4AMTDmOfG4EDkWV7Ju8ruR2nudhNBphNBoF6pmSzgU8QezPBSjX/nkozrkSPGT5VI7z+Tyy2awBD4EQ1H/7RbF1Icl9PM/zcR5yAglkW5kmaAhgG6y8hhRbtATlRmtuPB6fAChF1kPBeeKIGfu/KKCYdbxLH+Kx0oKR3EAqlcCxTiFfCKnHyH1S17GPlX2xwSL1IzmwUk+T++V/BJfNmSQwRqORAQ8Ba9+7dDkE0bmAJ4ii6CfzHBd2rE1y8OSDHQ6H6Pf7xpwdj8fGWsnn8wDgG2i7HeDY/yT1DHld2wKz25T3wgGUImcymRjxQjB4nmd0G15XgoLHSeCQ88iXR3LC+2mqn4rmBUhc7hW1LxykRCKBfr9vuMVoNEI2mzX6SCKRQCaTQS6Xc7YjOYdtYUnuJR2ctg4lOYrcx08JBG5sl3oZr0XxYzsfyXUkeHgc23wowRMGnFlAOC1QAJzgBAQPOQk9tFprA55sNovJZGL8PvaDtXWaIM7jOkZaZLR+uEndxhapkkNIq88+RwJOAocAcYFnOBw+nOCZl85Ckeb5tvfXdQwfdjKZ9IkKmsD5fB7D4RCe5/kGnoMW1LZ9PzzW1rmkOW5zGQ42uQxwDBaKWinibE+0rWxLB2WQfy2IHmrwnAWXmUV2TA2AActwOPTpGIeHhygUCibuA8DE1WRbUe/D5RR1xblc4KFXmKJPKsuAX3mXJrxLiZbHBLlPXPTQgud+AUcquTZwpAijLkDRQf9MsVhEqVTCcDg03l957rwkLSrp3aU+QvBQuaV4JQfRWps+yH5IEEj9yQ6h2I5byYlm0anAo5S6CaAJwAMw1lqfSMlgx4LI/s8ehLMGkYzluFz20o9iK7vJZBKj0QjNZhNaa5RKJbPJoKV02GmtDWci2Wa2NI+lLmNH2Sk6JRgkEFzix2XSUyzSHJfnUdRFAdBpOY8H4Me11gdhB7ETNkuPqxzP2459HuNEVISpxzAOxGNtZyBN2b29PWxvb6NWq2F9fR3JZBL5fN43EDI+ZvdPxq+kAizBI8MRkhO5uIMLNDI+JoGjtTapMGxT/md7nMPotOBRiJCNKBVVID6L57ny0247ynk0txnwlBFzmuASMByU4XCInZ0d7O7uYnd3F2tra0ilUqhWqwDgAwMj8rIt+TzseJUEjx34JPeRZrXsm4vDyPCDrddIMEoPs0uBDqPTgkcD+LKaZgv+ltb6M4EHOoBjWx32//Yx8ljJfaIA0dZ1GIbI5/Mol8uo1WqoVqsoFAq+hynfxE6ng8lkgnq9ju9///sYDoeoVqvY2NjweW9Ho5EJCXieZ0DEa8sBluCxgeMyy+WzswEjNwlEGWqwlXKbQ81DpwXPM1rrLaXUCoCvKqVuaK2/Zh/06quvmu/Ly8tYWlryPTyanfSQ2koryVZuSWFviQuoyWQSk8kE3W7XZOrt7u4azmO/hfwcDAbY29vDeDxGoVCA1hr1eh1vvPEGGo2G71oEJwOTrpgUPyUXsrkJRSCj+va9BW0S9OPxGP1+32ySI9mmeb1ex/7+foShP31KxtbR565S6guY5jCfAI9M+Tw63vdGSa+oTEHgm+ECTVBwUl4jaAOAbrdrBlQGEWUEWloiAEwaw2g08oGn1+vhrbfe8ineMhGLQVWplEtHoQ1waQUSPNls1qk7hnFvAmM4HGJ/f9+XvWkDlZx5eXnZl7LyxhtvBI5/bPAopQoAElrrjlKqCOAnAfxqlHMlZ6GzLZPJGPAwViO9p7Mcb65rhFkd8u2TVpdtKR3dKwAYxTifz6NQKBgRNhgMMJlMTCoHUyEYEyOAmN1HTsTNDmewP9J/YwdoXZ8uKxEAer0eRqMRWq2WT/zF1TtJp+E8awC+cKTvpAD8R631V+I0RLbMBCzP80xi/P0Aj61n8MHLt931RpMrMS10PB6j1+uh1Wqh3++jUCig1+uhUCgYkEjA2FzIBhC/28ny0hFoA8gOtHKToPU8z4BPRsvtl2Oe5wucLg31BwCuxT2fUWQAZlbC4uIiKpUKgGlGf6vV8rHUIGU7pI8nuIjUOWzQ2OBxcR6tp/Euvs0MUWQyGV9sCjj2VI9Go5m+JFew1AaMDRrZN3kviUTCzPKoVqs+01vqOA+S80QmWz/hDVJBLhaLWFhYwPLyMqrVKobDIZrNprFM7DbCbt6lD9ggkNFnOUDyPBd4EokEPM/z5cBQ7PF/gseOJc2KstscJIjTuriEC1S0ALPZLFKp1Alz/CzoXMMTknPw7WLWPjnP0tISms0mcrncCWXSxUlc1wjbz8EhF3GdN8vDKnNdqJNIS2hWNNq+pzBASNErj51FBE6tVjOqgMu6srn5PKLrXMETZhnJBKdsNoulpSVMJhM0m010u130ej30ej3fzUk9qVgshl7bZvWzWHZU7javnhDUfpg1yW04HKLb7aLT6aDb7Z64L3nsYDBAp9NBo9HAcDhEp9MxHFOCxL6+y6ILogeehgocu/0ZAMxkMlhaWkI+nzc+mN3dXfR6PXOOUtM83cXFRaysrGBlZWXm9VzgCeI+Ue9h1kMOG4ygawf1s91u4969ezg8PESr1fKJOB5D8UTAEDzdbteAh8e6RPwsF4ikhyKqbnMeZuqtrq6iXC5Da41ut4t6vQ7g+AYJnitXruDRRx8N1YfswZt1nP1Gu44Natt1jSCLxiUqgvSder0Oz/PQarWMc1UCTDpeJecZDAYnwBN07YeO88wiZvN3u11kMhlUKhUzrzqdTqPRaCCTyZwYBKm/2BFy2xsrKQoY5gEPz5l1jagiTl5fxqDC3BVUxpkgRmcrZ+f2+30zA9XVT7uPUfSfBwoevjWTycToM57nGZf+4uIitNYoFosmpCAtpMlkgkajgTt37mA8HmNhYQGVSgULCwuh4LGvb++TdFpzNiq5rkNRdXBwgIODA+zt7eHevXvodrsnTHh6tRkSoW+Jfh0ms0WltxXnYcxlPB5jaWkJmUzGgKdQKJhAI3DsqxmPx2g2m5hMJmi1WtjY2DDHuxLUXRRHz4lDUa5jX4/g2d7exu3bt7G3t4dOp4Ner3ciRzqZTJq5ZuVy+cQUmigpFvPSTPAopT4L4K8DuKe1fs/RvhqA/wzgEQA3Afy01roZpwPkIHSZ93o9PProo0in06jVaic4D7mF5DyNRsP4YPL5PJaWluJ05b5QVIXa5RrwPA/tdhtbW1t4/fXXTcDS5jrkPMViEbVaDSsrK+h0Omi1Wqbsyln2mRSF8/w2gF8H8Lti3y8D+GOt9b9S01qE//Ro36lJa41ms4nbt2+jUCiYDLq1tTW85z3v8dWPkf4Uz/PQ6XSwu7uLdDqNTqdj4lD5fP6EHiNpHl3E7qvre9C+WdfhiyHTQWTqKV8afjLGxinR5Lbtdhv9ft+Iqnk5aFSleSZ4tNZfU9MyKpI+AuBDR99/B8CfIgQ8Uc0/PphGo4Fbt25hMBggnU5jPB5jfX0d1WoV9+7dM5utAHY6Hezs7JggIJ2ODB3Ypu1ZURSfkRx0F7msJnvar21ak8suLy8jl8sZa7XZbPrmnMe5lyi+sLg6z6rW+t7RxbaVUqthB8sHN8vcJXiYtUc2vL6+jlqthtdeew2Hh4fY398/oSt0u12Mx2M0Gg20Wi1MJhNks1mT6Sc91mcFoCBnn9zH71EA5ErmkiEa2WYul8Pi4iIuX76MTCaDer2O3d1dNBqNU4ciztPPE3oll/cyyITVWpukJWCqFBeLRSQSCZMuyo1TUfiQB4OBmRLjeR7K5TIWFxcxGo1MGgRF17yueNn/sP1hDz3KC8SMgn6/b7zJw+EQWh8XQOAnvess/KSUMj4eXut+cFpSXPDcU0qtaa3vKaXWAeyEHXzjxrTmk9baZBJGYYsAMBwOUa/XkUwmjdMrkUhgfX0d+XwezWYTrVYL7XbbnMNBYL5Qr9fzFTniMQ+CZvl9xuMxWq0W9vb2UK/XUa/X0W63MZlMkE6nUSgUzFYqlXxcuNlsmilBQe3Pov39fRwchM5nMBQVPOpoI/03AH8HwK8B+HkA/zXs5Mcff/wEe4+qxA0GA5NwRWU4nU5jfX0d5XLZ1KthFJ5E/xHBw7eQSWdnQVHvIYquR6LOQvOcMT2Ch9yUlijBw9yi04JncXERi4uL5vcPfvCDwGOjmOq/B+DHASwppX4I4BMAPgngD5RSfw/ALQA/HbVzkuNE4T6cJrK3twelFDY3N7G5uYn19XUzIU7mD7Nd6g2sesEc6bP2dcxDdh9dehBfhK2tLdy8edN3DrnN0tISNjc3jfOw0Wig1+v5dJzz4KxRrK2fDfjrr0S9SFSdAHCbw3IDjvNxlFKoVCpYWVnxlQ+hldHr9YyYo3eaZVKi9DXKcfOYwS5djzper9dDv983QeBut3vCUpLJZZzyLHOS2Z/zEskPRUpGGFHcAPApjPy+sLCAyWSCVCqFZrNpNoInkUhgNBpBKYVcLoeFhYVz7b/rfuQnvch7e3vY3d1FvV7HwcGBEbXyxZFi2PblPAg6N/Cc5sHT/W5XvGIQNZVKoVQqYXt7G57nodvtmrd5PB6j3W4b4LiCg3H7HfeeJIC01uh0Otje3sbNmzdxcHBguKgNHgaQCR7O+nxQoviBx7ZmORDlg5ZpnsPh0CSi5/N5LC4umol5rOjF45RSPqssl8v5kszt68UBzDxAkjNLh8OhyVna3t42eToyY4AiOpvNQilllGM54zPq83T1N66Ye2DgCfL1zBq4wWBgLCsmeFerVVQqFbRaLWxtbZk8Y5ls3u/3sbe3h2QyiW63a6LvTLiXfQpS6qOEIKLcK++h1Wrh4OAA9+7dQ6PR8IVbyGlYNLxYLPrm0dsOxAdBDzwlg2R7aF0RZgDGeUjHGaPIly9fxtbWlpnxSfFEEdfv91Gv102G3fr6OlKpFMrlsq+sW5CH2EWzDIGge6Hv6u7du9ja2jLOQE5wlMaBzJZMp9PGdO/1es6c5NNQVK5FeuBii+TyQsvf/E4vcqvVQiqVwpUrV1CpVHDlyhW8+eabBjzUGcjyGVDd399Hq9VCMpk0XCco4BnVkTnv4NF3devWLeNHsfUgcpRcLodarYbLly8jlUphd3f3xMS9swIPKSqIzg08UVMTgsxZEqe0eN50DYv9/X3cuXMH+XwerVYL2WwWly5d8k1bpilL932/30ej0cDOzo5JomeZFVko6bQkzWbZDwKZWYIyaMs57kzsqtVqSKfTJq2CGYGzgBP2vF1hkjjZBuc6byuIwvQM129+HwwG2NnZQSKRQKfTQbPZRCaTwdWrV7G4uGicaAcHB762mTx29+5dDAYDLC0tYWlpycwli3N/s3Q1WeWLEwa11ifCJZlMBtVq1VTtILAODg5McQaK7NOSLaLnVZwfCrE1S1F1/QaOwdPtdrG9vW2qdF29ehX9fh+3bt3CZDI5UfWBXtzBYICDgwMMBgMkk0mUy+VT3QPg1tVoIQ4GA6OvkHvYZXQJnkuXLmFjY8MkuzUaDfT7fcPBXNc6b4qbSfgJAL+A44Dor+jpIiZBbYRew3bTRwUQ2X6z2UQikcCVK1fM7NNyuWzyfwuFgm+6LR2InMpDf9HS0hJKpZIxlW09JC5pfTxFmVbWYDDwzYDglsvlUCqVUK1Wsby8bEx5ztWy+xaHop57FmLLlUkIAJ/SWn8qUi9mkCvOE6Q4uwaSCiYzCTl/nEnxjz32GNrtNjqdjklxkNcej8fodDqo1+tIJBK+FWPmBY7rgTME0Wg0cO/ePRwcHKDVahkflFxNsFKpIJFIoNfrYWdnB81mE/1+/4Ga5EEUN5MQ8EfZQylMew8CTpgfKMj30u12Td4vAVCtVrG6uoqdnR2TZUjw8A0meCje6P+hUy4KsV/cbB2t3+/j4OAA29vbRmSyH5lMxuQoMdmfkXRyKRoKp+U6Z0mn0Xl+USn1cwD+D4B/rGMkwNtiYRaAXMcCx3oFOQsAlMtlbG5uYnV1FZubm0in0xiNRj79R4KHkwo5SNlsNvJ92CCXAOI2GAzQaDSwvb3tyz1iORRGy5l2SxEnQxBnKUrPguKC5zcA/AuttVZK/UsAnwLw94MOvnHjhrnR5eVl39RgUpB+M6/TjroNi0pSFNCC4Sp/dvFIOh9ZtcOeXRmVeA4j34PBAO12G7u7u0ZUydrOMhRB5ZkxLBaNkkUV7M+oHm5XH110P5LB7Ivvip+fAfDfw45/4oknYg1E0MMJ41RMNbXLu3FaSr/fN1mJ3Fizj0WQpC8laj8lkdMwE7Ber2Nvbw/tdtvoY9K3AxzP16d3XMatbP0vyjOKS5w0QHrzzTcDj42VSaiUWtdabx/9/FsA/t/83Yx44RkPx+ZQfJPtZa5LpRJqtZp566lQM8WTg8Y4mD1wUUmGUer1On74wx8afxJ1F7toExV+zkuT4JFtBinjZwkgm7uFUdxMwp9QSl3DtIj3TQAfjdopF4V5OqOY8a4bthfnSKfTqFQqBlh0uNFpSKKySpHD67oSyW2RKmvgtNtt1Ot1bG1t4fbt2ydElF2BnqIUOK7/wzydoAGd5SEOolnHRgVQ3EzC35513llTFDNeEi2V7e1taK2Ny39lZQX5fN6YzuRC5DIyDdTzPLOOerlcDp3CTFcBN0bKZU4x+8lcZEbMCSpZe5kKsrz/sOfyIOiBhSdOowMFmfGSOAtB62l5lvX1dWxsbGBlZQXVatVYPpwDzzZZUIrcY3V1Faurq2bh2iAieOgS2N/f94FHWobkgqurq1hcXESv10O32zVlUIIm+oU9j3npLAD30OTzzHverPPJebrdLnZ3d5HL5XDp0iWsrKwgkUhga2vLzAeTnIGch0Bg0hknDgaRdFLeunUL7Xbb+JRk+1TKK5UK1tbWsLm5iZ2dHQNa24EZ9XnMS2FcOyo9UM4TBQguUz3KG0cuQj2CiVe7u7vIZDKYTCbI5/NYW1sz+cBMKpf5QM1mE/V6HcViEVprn/eZSi71p1arhVarZSpZUP+h34iRci5ToJQyfhyKKlv5D6Mo3CnquXFA9EDAE2Rmy//s411tznPD7XYbd+7cATDNkWHRzEceeQT7+/vY29sz/hVJNLmB6Vx4RuCz2ayJkXW7XZN4zwIMsghlIpEw61vUajVTaZ5gJXh57HmQDZowYyCIHlgp3TAAyfPCOFPUNxM4Bk+r1TL1e/L5PKrVqlk/lN5pSTS5uU4F578vLi4ajnNwcIB6vY5ms2nCChI8jNivra3h8uXLUEoZLtVut30+nbPSD6NSHK5FOjfwuLjLPADi96hkg44VVXd3d1EsFs3kwbW1NaNc1+t1U+VdrttAk73ZbCKfz6NWq5n8HMbE6vW6L1pO4LDfPG9jY8N4n5lXLV0B83iDTzPwZ0HnmkkYxnmCKKoYi3Jdnktxs7+/D6UUer0estks1tfXUSgUTPqDnHjHPvR6PdTrdbz11ltGpO3v7xuRFTQVhq6B7e1to8wzVdal4wS9MKfhQmcNzHMv4i0pTNeJy22iXJfiBpjGoBic3NjYQK1Ww97eHnZ2doweIs1sijGllKlUT+tMrsYnr8twRaPRMMXDaZZL5yHPiaMD2vdrH+PiarPamEVRPMyXMc3lWcPUo/wZrfW/VacsLTdLYSPNcs3bbUZ5Mw8PD006Z7vdRrVaxdLSkpngzxDF/v7+CT2ECWQMYZBDUbTZ/eK5zFpkVVM6AyV4bA4UxpVnvShhALI5cdD5sygK55kA+LjW+iWlVAnAnyulvgLg7yJiabmwgXdxm7Bzg8Rd0ENwEU1xVgktlUpm1mkqlcLBwQFKpRIKhYKJR1GPkRPuZE0gWepWKf8CuFykhRxILssUxHmC7j2MwgY+SKeS15fFr6JcL0p4YhvA9tH3jlLqBoDLmKO03CxxNQ+52HocolLMduTMBa49WqlUzIrGTKWgDiQLZksTmwORTqfNbFbmBhEwNvDtQQ+7t1kcwcXB5KcLPLKONZ9LlKDwXDqPUupRTJdJ+jMAazpiabkgUz0uuay2OCT1GbnicT6fN/EskixLK9MnXI49ch4uyML8IC5xbZ8j7ynoPl375X3IaweBx3Uu+8rsA74UUWajRgbPkcj6QwD/6IgD2SMWOIKzlMA4b5h97jwgsnUT2UYymUQul0OxWES1WjXWGae7BK2II1m/UlOPskzGp4LuCnoG3XcYaHi/LuC6NtczIMeUBcDl7IxZq/dEAo9SKoUpcD6ntWYVsMil5V5++WXT4bW1NaytrZ2p4yuuKON5VGaZ9zMej1GpVIz4SiaTZv0Gkv0CsEYgN1axZ8yLWYGuFyeKKAp6weS9ywQze/VAud6XFE3AcekarTXu3LmDO3funKnY+g8Avqu1/jdiX+TScteuTRcElDLffgguERQFDPa5szia63xOb5lMJqhUKr4iCJytyRBFUBuc976ysmIWeGUCGEMWEjy2UjzrXsNEGDcJknQ6bcQRc4b43RZNcltfX8fy8rIR0d/5zncC7zuKqf4MgL8N4BWl1IuYiqdfwRQ0/0VFKC1na/E2zZLpUR6sDaB59CFyhXa7jW63i3w+j0qlgne+850Apnm9MiHeBjgHrlwuY3V1Fe94xztMKWDW0nH1OexegsgW/VLhl5zGXl1Zrjlqr9cuazZLIJ2FtXUdQNAqIJFKy1ERszsWppC5OIiLM9n/RQGOPXC0mobDoZm6zOKQWk8TybgSoSxfZ+dIM2FMigZyHClWwsRUEBeVfXcpxa7sRDvdRD5zcidei32N0kfSuXiY8/m8b6K/ZN9SAXWJLEkuvWYWgOSxUYh5NZT73W4XWk9LACeTSTPjk1F5irdyuWwCrLu7u+j3++h0Oj5H4DzkAr/kLJzjbiu+FE08n/6o8XhsplW7VlXmiyDBdGbW1mkon8+bGxiNRgDgq6Nnd9KlUIZxkygAsikIUKwgz9X0uJQ1F8/d3t6GUtOSLcViEUtLS1hfX8fCwoKZwswAKZ2H0gc0D9nHS4DY3JychJsUTfaEQeYj5XI5AyJZ4EH6sMLoXMCTy+WMB9bmMHxrbKedi8KANA+AwoBIztNut5FIJLCysoKNjQ0sLy8jm81Ca21CF4VCwZS1rdVquHv3rinALfOC5snRCbt/aVbncjkzwEyjlWu3E7gy3saNedMEmqzUIcXXrH6fC3hY3UGWQnMpZK4BncVBSC4/UhBIgkSi/Z984Nx4H7TQONuiVCqZaDwHM6ifYWQvoy1FjNSxMpmMb4oO75W6G7MT+XLKduj55oIu1MsINHrNZz3zcwOPZIVx9Zwgcpm/s0TXrHbZlj3YEjzMyWFqq9QhoprgNtm6C7kJuYT8j4qPGE8HAAAMsUlEQVQ7AUCuobU2+iXvU64CKC0v9o9xOteUnyA6N/C43uIg/YXk4ib2sXKQo3Ie+zqSXKCR+yR4qBBTJDPNlNW85DXsvgb1h7oLB5u6CVNXJQdhkJVErmGv0UXTnRXkaZUlk0nzIrMyqywG/lCILbvKp/wkud5QlzNtFqCicCqb5jGP5VRhro3K6hyMZ9k+GNd9ua4hryUXnKWOY68bxvUoJJehSkCPMQBfqTppicmlJKUTU/YjjB5IDnPYGzhPW3HE0jxciP/RCUiRweCpjHcdHh76lmWK2r78n9eSA2uv1Mfvcj+5Fa0mLpHgAjz7zE2KK5tTzqI4yWC/pbX+dTVHdTCbZccBjavNIJrFnaKcI6/j4gJcwlK6+u01vex+BvVDcjYeIyP3dt/kRmDLdgC/4i39PVSkpaUWVokjjOImg3316L9I1cHmVRrDznWZ6C4Ksp5m6UA22Ageae1IzkPwjEYjozQHiaUgF4PkEJLz8FOuZGMbGza45bry3FgZn1XR5FrttmU4j8iPmwx2ideKfCXRuaCBlfvCzOsgXSLoeB4XJObCQM1B4gCyitfy8rLPUqFiKkMC8jPs+tKUtv+jIsu0WenmsJe8lkFQGWbwPM8UbrCtXdmHIPUiiOImg30TwLOIWB0sDAhyXxBHOQsxdxqSD5rFolj8iTrDeDz2gScq+7c5G5+DtIKYH82CDK44oVLKZ8rLflMEBvnZZB+k0n1m4FEnk8Hmqg7m4jZyP/+bJVJc/80DrnmP53X5dmezWZNhyILcnPFJ8Nj9ltd1XZ8DR/NemtnSb8NrysGV4kv6g2S5FwkECUx5ffZhnppEsZPB9BzVwb797W+b75ubm9jY2PANSNTOxgGefe4s5X2W5ZVKpZDL5aC1NoUz+ca7OE+U++A+l9iQaa+SK0h/DHCc9iJFmcyxlon4NOVl/jX7zXpC9zUZTM1RHezpp5/2KXYAfGxUPoQ4FEWXsa8vB2GWQm+HDGzTWu4PA04QwAkOHiM5ht2ejHbbJry8H3uuvHQ6SnFm+3rW1tawurpqzmcWqItOkwz2sypidTBb+5f+BumYOg3ZALJFhNQrgGMl16XAu6whGyDyfxewwvpJsjmMzRFlv6QJ7+KY/M/uPwDjYS4WiyiVSuYYgpaV0ORs11ncEzhdMlhgxfcTFxEmZDqdNizWdkydllwAkv+5lFJX2oENKBsg8jgbOPPcjwRE1KR4+77kPplkZ/c7m82iUCiY0noEIIOqBI6dvhFG5+JhrtVqTrEBTB8M/Q1Bg0mKarXZYsX2odiWhus6YTqUS0zNsrDigGreY+V3esLlVCIm5gN+I6BYLAKAyW9+6MADnPSZkBPQcUXzN4gtz3oDJUjsNARbiZTgDWvP1YcgjhPFRI8CjKBjXIB3XU8pZQqDl8tlsyQUwSQVcWC65LaMy0WlcwEP1/+UipmdekAfhiuIGkT2wMsBlaV00+m0L8dFmsIuHcneZ/fF5mZhImteq0vul+Il6Lig69KZycVY5ItE7iKTyAqFwon7PFMnYVzK5/MmbYEdpxLHuIzNFaIugRhk+UgFmaVzeR2Z9moD0AUclyicxySPC6CgvtnHuNpgJN1Wkkl87nZYYx46F/BQJHEeE0uLAPABicCS00GigMceTKmIytmPs2Zr2IoyuZkNSlt5lv4X2Z78nIeCQOISqzaXssn2GNv6Hn0/dDBGcTmQzgU8nKMti0bKOAzBo5Qy5ftlVNlFcmDtmBL/JweTMn6WLmUPgi2eXGa57fGNA5ggcuk3tu4TBCDbn0PVQeqDMlsxm82emFkRRucOHs6HYk1j6Zll1JpmvF1ckuQaXFZ44P/yLVNK+dIbgsg1CC5xaIPH5fI/LYBmWW5BILX1JH5nhuF4PPYFTmWmgPSWc1zC6FzFFjtP77IcBNvjKSenBbFj+7dtqfEBU9eSFlaQDmGfJ/eFKa+yjbMSWfPoU1K/S6fTWFhYQKFQMBmEFE+Hh4cGMDQmZF6zBM5DwXkIHLtEiXx7ZXISp77KAbQBAcD55tsDLEVLmG9HUpip7AKp5EwufSEqiOL0S4Inn8+jUCgYZ2C5XPbVByLZTlv5aRdFCKMo4YksgP8FIHN0/B9qrX9VTdMzfh/AIoA/B/BzWmtnTQ5yHpnBJkFBtmpnuAU9MJtsMWUPrDwmqM0gH4+L8wQprrO4TlzQhh3Pc1KpFPL5PBYWFgzXKRQKZoqN1GNkuIgizA7qnonCrLUeKqV+QmvdU0olAVxXSv0RgI8D+Nda6z9QSv0mpukY/y6gDZ9uwhv3PM/MaJTFk4IG2hY1QQNriy77gUcll7ksrxf1vLjXj9I3blyYLp/Pm6nP2Wz2BIexMw1d1mNUiiS2tNa9o6/Zo3M0gJ8A8DNH+38HwD9HAHiKxaLPd0PRxM2Vn+IiF3Di6Bg2CGdZSK72XZzOVrLnJduacv1n90daguwTE9OCrCbZX3Ie+WLL48Ioaj5PAlPR9CMAPg3g+wAaWmva0bcBbAadz+mtvGHP80z1c84VciUt8fhZIsU1WGEDISkIOEHXtEWkK+vuLBTloPbseybXIUBoVQWBx345+R/BY1trYRSV83gAfkwpVQHwBQA/GuU8EqtrkWXS6hmNRmbpxLBUA0lhukWQqW37Pk4jutiGzXnmAVAUUeqyCF0vjS1ypAowmUyQSqV8wWa7j7an+czBIy7cUkr9KYAPAKgqpRJHwLoM4E7QeZ///OfNDV67dg3vfve7fcne8zxMl3yOIu5cCrTrWlEemg0ctjNL2Qy6ZlQFNegc13kUX/zOvGZyflvc8gX++te/juvXr0fqQxRraxnAWGvdVErlAfxVAJ8E8CcAfgrTQt4/j5Cycs899xy++93v4tq1az7O43oQLqWND+fu3bu4cuWKsQ6A45hYmJiz6e7du9jcPJay9tsYdj4f9o0bN7CwsHCi/64BDQLN1tYWNjc3nffuOj+ovdu3b+Pq1au+vhA8tGLz+bxTrwGmz/D69ev40Ic+hPe///34wAc+YNp6/vnnA59FFPV6A8CfKKVewnTWxJe11v8D05rLH1dKvYapuf7ZoAaUUqa2XZgVFPQWcf/W1taJWEwUZ5ZNW1tbzvajEN/S11577YTuMKv/9sZaP9JUlhZRmHUk2+FSULIvBI8MCbmqm/J+vvGNbwRavEEUxVR/BcBfcuz/AYCnZ50PzBYNUr67dBKbM8mC07x52c6sPoRxhqhiK0hkudoPIhtMcrap3T/XFgZU2/3BWoQuUHCf1I2i3MP5rAx2nynKgF/Q2ZO63w9enSz2fUFvM9JaO1nQfQfPBf3Fpb8QYuuCHgxdgOeCYtN9B49S6sNKqe8ppV5T03W54rZzUyn1f5VSLyql/nfEcz6rlLqnlHpZ7Ksppb6ilHpVKfVlpdRCzHY+oZS6rZT69tH24RltXFZK/U+l1HeUUq8opf7hvP1xtPEPYvYlq5T65tGzfEVNay1BKfWoUurPjsbqP6npNPNgCjIDz2LDFJxvYLoaYBrASwB+NGZbbwKozXnOs5hW9XhZ7Ps1AP/k6PsvAfhkzHY+gWndoqh9WQdw7eh7CcCrmIZ5IvcnpI25+nJ0fuHoM4npElhPY+rw/amj/b8J4KNhbdxvzvMUgNe11re01mNM838+ErMthTk5pdb6awAOrN0fwTQLAEeffyNmO+xT1L5sa61fOvreASAXvYvUn4A2YtVK0sGZEp8XffmbYW3cb/BcAvCW+H0bxzc7L2kAX1ZKfUsp9Qun6NOqFovMAQhcZC4C/aJS6iWl1L+PIv5IappI51z0Lmp/RBvfjNMXpVRCTWsPbAP4KubMlADeXgrzM1rr9wL4a5g+qGfPqN24vorfAPAjWutrmA7AzPJ6AKCsOkeO68/sj6ONufuitfa01j+GKfd7CnNmSgD3Hzx3ALxD/A6NvoeR1nrr6HMX07SQp2L26Z5Sag0A1IxF5mb0Z1cfO8k+A+B9s85RIYveRe2Pq404fRH30cJ0fViTKXH018yxut/g+RaAx5RSjyilMgCew3SRt7lIKVU4etuglCoC+EmE1AOyT4dfH+Aic8CMbICwdo4GmhRan0hQ2KJ3UfvjrJU0T1+UUssUbeo4U+K7OM6UiNaX01pUEbT6D2NqFbwO4JdjtvFOTC21FwG8ErUdAL8H4C6AIYAfYrqcdw3AHx/16SsAqjHb+V0ALx/16wVMdZewNp4BcCju49tHz2Yxan9C2pi3L+8+Ovelo/P+mXjO3wTwGqaWVzqsnYvwxAXFpreTwnxBDxldgOeCYtMFeC4oNl2A54Ji0wV4Lig2XYDngmLTBXguKDZdgOeCYtP/B0Mo1Uy+QKu5AAAAAElFTkSuQmCC
"
>
</div>

</div>

<div class="output_area">

<div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>INFO:tensorflow:Restoring parameters from ./traffic-signs-classifier
TopKV2(values=array([[1.        , 0.        , 0.        , 0.        , 0.        ],
       [1.        , 0.        , 0.        , 0.        , 0.        ],
       [0.9431515 , 0.02619995, 0.02196108, 0.00440191, 0.00139556],
       [1.        , 0.        , 0.        , 0.        , 0.        ],
       [1.        , 0.        , 0.        , 0.        , 0.        ]],
      dtype=float32), indices=array([[13,  0,  1,  2,  3],
       [28,  0,  1,  2,  3],
       [11, 18, 27, 30, 21],
       [17,  0,  1,  2,  3],
       [18,  0,  1,  2,  3]], dtype=int32))

        [Prediction]
Sign 1: Yield

Sign 2: Children crossing

Sign 3: Right-of-way at the next intersection

Sign 4: No entry

Sign 5: General caution

</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Analyze-Performance">Analyze Performance<a class="anchor-link" href="#Analyze-Performance">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[41]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">### Calculate the accuracy for these 5 new images. </span>
<span class="c1">### For example, if the model predicted 1 out of 5 signs correctly, it&#39;s 20% accurate on these new images.</span>
<span class="n">output</span> <span class="o">=</span> <span class="p">[</span><span class="n">out</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="mi">0</span><span class="p">][</span><span class="mi">0</span><span class="p">],</span> <span class="n">out</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="mi">1</span><span class="p">][</span><span class="mi">0</span><span class="p">],</span> <span class="n">out</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="mi">2</span><span class="p">][</span><span class="mi">0</span><span class="p">],</span> <span class="n">out</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="mi">3</span><span class="p">][</span><span class="mi">0</span><span class="p">],</span> <span class="n">out</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="mi">4</span><span class="p">][</span><span class="mi">0</span><span class="p">]]</span>
<span class="n">correct</span> <span class="o">=</span> <span class="p">[</span><span class="mi">13</span><span class="p">,</span> <span class="mi">14</span><span class="p">,</span> <span class="mi">11</span><span class="p">,</span> <span class="mi">20</span><span class="p">,</span> <span class="mi">27</span><span class="p">]</span>
<span class="c1">#print(output)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;It&#39;s </span><span class="si">{}</span><span class="s2">% accurate on these new images.&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span> \
<span class="n">np</span><span class="o">.</span><span class="n">average</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">equal</span><span class="p">(</span><span class="n">output</span><span class="p">,</span><span class="n">correct</span><span class="p">)</span><span class="o">.</span><span class="n">astype</span><span class="p">(</span><span class="nb">int</span><span class="p">))</span> <span class="o">*</span> <span class="mf">100.0</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>It&#39;s 40.0% accurate on these new images.
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Output-Top-5-Softmax-Probabilities-For-Each-Image-Found-on-the-Web">Output Top 5 Softmax Probabilities For Each Image Found on the Web<a class="anchor-link" href="#Output-Top-5-Softmax-Probabilities-For-Each-Image-Found-on-the-Web">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>For each of the new images, print out the model's softmax probabilities to show the <strong>certainty</strong> of the model's predictions (limit the output to the top 5 probabilities for each image). <a href="https://www.tensorflow.org/versions/r0.12/api_docs/python/nn.html#top_k"><code>tf.nn.top_k</code></a> could prove helpful here.</p>
<p>The example below demonstrates how tf.nn.top_k can be used to find the top k predictions for each image.</p>
<p><code>tf.nn.top_k</code> will return the values and indices (class ids) of the top k predictions. So if k=3, for each sign, it'll return the 3 largest probabilities (out of a possible 43) and the correspoding class ids.</p>
<p>Take this numpy array as an example. The values in the array represent predictions. The array contains softmax probabilities for five candidate images with six possible classes. <code>tf.nn.top_k</code> is used to choose the three classes with the highest probability:</p>

<pre><code># (5, 6) array
a = np.array([[ 0.24879643,  0.07032244,  0.12641572,  0.34763842,  0.07893497,
         0.12789202],
       [ 0.28086119,  0.27569815,  0.08594638,  0.0178669 ,  0.18063401,
         0.15899337],
       [ 0.26076848,  0.23664738,  0.08020603,  0.07001922,  0.1134371 ,
         0.23892179],
       [ 0.11943333,  0.29198961,  0.02605103,  0.26234032,  0.1351348 ,
         0.16505091],
       [ 0.09561176,  0.34396535,  0.0643941 ,  0.16240774,  0.24206137,
         0.09155967]])</code></pre>
<p>Running it through <code>sess.run(tf.nn.top_k(tf.constant(a), k=3))</code> produces:</p>

<pre><code>TopKV2(values=array([[ 0.34763842,  0.24879643,  0.12789202],
       [ 0.28086119,  0.27569815,  0.18063401],
       [ 0.26076848,  0.23892179,  0.23664738],
       [ 0.29198961,  0.26234032,  0.16505091],
       [ 0.34396535,  0.24206137,  0.16240774]]), indices=array([[3, 0, 5],
       [0, 1, 4],
       [0, 5, 1],
       [1, 3, 5],
       [1, 4, 3]], dtype=int32))</code></pre>
<p>Looking just at the first row we get <code>[ 0.34763842,  0.24879643,  0.12789202]</code>, you can confirm these are the 3 largest probabilities in <code>a</code>. You'll also notice <code>[3, 0, 5]</code> are the corresponding indices.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[42]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">### Print out the top five softmax probabilities for the predictions on the German traffic sign images found on the web. </span>
<span class="c1">### Feel free to use as many code cells as needed.</span>
<span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">out</span><span class="p">[</span><span class="mi">0</span><span class="p">])):</span>
    <span class="nb">print</span> <span class="p">(</span><span class="s2">&quot;Image </span><span class="si">{}</span><span class="s2">: </span><span class="si">{:.9f}</span><span class="s2"> </span><span class="si">{:.9f}</span><span class="s2"> </span><span class="si">{:.9f}</span><span class="s2"> </span><span class="si">{:.9f}</span><span class="s2"> </span><span class="si">{:.9f}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">i</span><span class="o">+</span><span class="mi">1</span><span class="p">,</span><span class="n">out</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="n">i</span><span class="p">][</span><span class="mi">0</span><span class="p">],</span> <span class="n">out</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="n">i</span><span class="p">][</span><span class="mi">1</span><span class="p">],</span> <span class="n">out</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="n">i</span><span class="p">][</span><span class="mi">2</span><span class="p">],</span> <span class="n">out</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="n">i</span><span class="p">][</span><span class="mi">3</span><span class="p">],</span> <span class="n">out</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="n">i</span><span class="p">][</span><span class="mi">4</span><span class="p">]))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Image 1: 1.000000000 0.000000000 0.000000000 0.000000000 0.000000000
Image 2: 1.000000000 0.000000000 0.000000000 0.000000000 0.000000000
Image 3: 0.943151474 0.026199950 0.021961084 0.004401913 0.001395559
Image 4: 1.000000000 0.000000000 0.000000000 0.000000000 0.000000000
Image 5: 1.000000000 0.000000000 0.000000000 0.000000000 0.000000000
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Project-Writeup">Project Writeup<a class="anchor-link" href="#Project-Writeup">&#182;</a></h3><p>Once you have completed the code implementation, document your results in a project writeup using this <a href="https://github.com/udacity/CarND-Traffic-Sign-Classifier-Project/blob/master/writeup_template.md">template</a> as a guide. The writeup can be in a markdown or pdf file.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<blockquote><p><strong>Note</strong>: Once you have completed all of the code implementations and successfully answered each question above, you may finalize your work by exporting the iPython Notebook as an HTML document. You can do this by using the menu above and navigating to  \n",
    "<strong>File -&gt; Download as -&gt; HTML (.html)</strong>. Include the finished document along with this notebook as your submission.</p>
</blockquote>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<hr>
<h2 id="Step-4-(Optional):-Visualize-the-Neural-Network's-State-with-Test-Images">Step 4 (Optional): Visualize the Neural Network's State with Test Images<a class="anchor-link" href="#Step-4-(Optional):-Visualize-the-Neural-Network's-State-with-Test-Images">&#182;</a></h2><p>This Section is not required to complete but acts as an additional excersise for understaning the output of a neural network's weights. While neural networks can be a great learning device they are often referred to as a black box. We can understand what the weights of a neural network look like better by plotting their feature maps. After successfully training your neural network you can see what it's feature maps look like by plotting the output of the network's weight layers in response to a test stimuli image. From these plotted feature maps, it's possible to see what characteristics of an image the network finds interesting. For a sign, maybe the inner network feature maps react with high activation to the sign's boundary outline or to the contrast in the sign's painted symbol.</p>
<p>Provided for you below is the function code that allows you to get the visualization output of any tensorflow weight layer you want. The inputs to the function should be a stimuli image, one used during training or a new one you provided, and then the tensorflow variable name that represents the layer's state during the training process, for instance if you wanted to see what the <a href="https://classroom.udacity.com/nanodegrees/nd013/parts/fbf77062-5703-404e-b60c-95b78b2f3f9e/modules/6df7ae49-c61c-4bb2-a23e-6527e69209ec/lessons/601ae704-1035-4287-8b11-e2c2716217ad/concepts/d4aca031-508f-4e0b-b493-e7b706120f81">LeNet lab's</a> feature maps looked like for it's second convolutional layer you could enter conv2 as the tf_activation variable.</p>
<p>For an example of what feature map outputs look like, check out NVIDIA's results in their paper <a href="https://devblogs.nvidia.com/parallelforall/deep-learning-self-driving-cars/">End-to-End Deep Learning for Self-Driving Cars</a> in the section Visualization of internal CNN State. NVIDIA was able to show that their network's inner weights had high activations to road boundary lines by comparing feature maps from an image with a clear path to one without. Try experimenting with a similar test to show that your trained network's weights are looking for interesting features, whether it's looking at differences in feature maps from images with or without a sign, or even what feature maps look like in a trained network vs a completely untrained one on the same sign image.</p>
<p><figure>
 <img src="visualize_cnn.png" width="380" alt="Combined Image" />
 <figcaption>
 <p></p> 
 <p style="text-align: center;"> Your output should look something like this (above)</p> 
 </figcaption>
</figure>
 <p></p></p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">### Visualize your network&#39;s feature maps here.</span>
<span class="c1">### Feel free to use as many code cells as needed.</span>

<span class="c1"># image_input: the test image being fed into the network to produce the feature maps</span>
<span class="c1"># tf_activation: should be a tf variable name used during your training procedure that represents the calculated state of a specific weight layer</span>
<span class="c1"># activation_min/max: can be used to view the activation contrast in more detail, by default matplot sets min and max to the actual min and max values of the output</span>
<span class="c1"># plt_num: used to plot out multiple different weight feature map sets on the same block, just extend the plt number for each new feature map entry</span>

<span class="k">def</span> <span class="nf">outputFeatureMap</span><span class="p">(</span><span class="n">image_input</span><span class="p">,</span> <span class="n">tf_activation</span><span class="p">,</span> <span class="n">activation_min</span><span class="o">=-</span><span class="mi">1</span><span class="p">,</span> <span class="n">activation_max</span><span class="o">=-</span><span class="mi">1</span> <span class="p">,</span><span class="n">plt_num</span><span class="o">=</span><span class="mi">1</span><span class="p">):</span>
    <span class="c1"># Here make sure to preprocess your image_input in a way your network expects</span>
    <span class="c1"># with size, normalization, ect if needed</span>
    <span class="c1"># image_input =</span>
    <span class="c1"># Note: x should be the same name as your network&#39;s tensorflow data placeholder variable</span>
    <span class="c1"># If you get an error tf_activation is not defined it may be having trouble accessing the variable from inside a function</span>
    <span class="n">activation</span> <span class="o">=</span> <span class="n">tf_activation</span><span class="o">.</span><span class="n">eval</span><span class="p">(</span><span class="n">session</span><span class="o">=</span><span class="n">sess</span><span class="p">,</span><span class="n">feed_dict</span><span class="o">=</span><span class="p">{</span><span class="n">x</span> <span class="p">:</span> <span class="n">image_input</span><span class="p">})</span>
    <span class="n">featuremaps</span> <span class="o">=</span> <span class="n">activation</span><span class="o">.</span><span class="n">shape</span><span class="p">[</span><span class="mi">3</span><span class="p">]</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">figure</span><span class="p">(</span><span class="n">plt_num</span><span class="p">,</span> <span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">15</span><span class="p">,</span><span class="mi">15</span><span class="p">))</span>
    <span class="k">for</span> <span class="n">featuremap</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">featuremaps</span><span class="p">):</span>
        <span class="n">plt</span><span class="o">.</span><span class="n">subplot</span><span class="p">(</span><span class="mi">6</span><span class="p">,</span><span class="mi">8</span><span class="p">,</span> <span class="n">featuremap</span><span class="o">+</span><span class="mi">1</span><span class="p">)</span> <span class="c1"># sets the number of feature maps to show on each row and column</span>
        <span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s1">&#39;FeatureMap &#39;</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">featuremap</span><span class="p">))</span> <span class="c1"># displays the feature map number</span>
        <span class="k">if</span> <span class="n">activation_min</span> <span class="o">!=</span> <span class="o">-</span><span class="mi">1</span> <span class="o">&amp;</span> <span class="n">activation_max</span> <span class="o">!=</span> <span class="o">-</span><span class="mi">1</span><span class="p">:</span>
            <span class="n">plt</span><span class="o">.</span><span class="n">imshow</span><span class="p">(</span><span class="n">activation</span><span class="p">[</span><span class="mi">0</span><span class="p">,:,:,</span> <span class="n">featuremap</span><span class="p">],</span> <span class="n">interpolation</span><span class="o">=</span><span class="s2">&quot;nearest&quot;</span><span class="p">,</span> <span class="n">vmin</span> <span class="o">=</span><span class="n">activation_min</span><span class="p">,</span> <span class="n">vmax</span><span class="o">=</span><span class="n">activation_max</span><span class="p">,</span> <span class="n">cmap</span><span class="o">=</span><span class="s2">&quot;gray&quot;</span><span class="p">)</span>
        <span class="k">elif</span> <span class="n">activation_max</span> <span class="o">!=</span> <span class="o">-</span><span class="mi">1</span><span class="p">:</span>
            <span class="n">plt</span><span class="o">.</span><span class="n">imshow</span><span class="p">(</span><span class="n">activation</span><span class="p">[</span><span class="mi">0</span><span class="p">,:,:,</span> <span class="n">featuremap</span><span class="p">],</span> <span class="n">interpolation</span><span class="o">=</span><span class="s2">&quot;nearest&quot;</span><span class="p">,</span> <span class="n">vmax</span><span class="o">=</span><span class="n">activation_max</span><span class="p">,</span> <span class="n">cmap</span><span class="o">=</span><span class="s2">&quot;gray&quot;</span><span class="p">)</span>
        <span class="k">elif</span> <span class="n">activation_min</span> <span class="o">!=-</span><span class="mi">1</span><span class="p">:</span>
            <span class="n">plt</span><span class="o">.</span><span class="n">imshow</span><span class="p">(</span><span class="n">activation</span><span class="p">[</span><span class="mi">0</span><span class="p">,:,:,</span> <span class="n">featuremap</span><span class="p">],</span> <span class="n">interpolation</span><span class="o">=</span><span class="s2">&quot;nearest&quot;</span><span class="p">,</span> <span class="n">vmin</span><span class="o">=</span><span class="n">activation_min</span><span class="p">,</span> <span class="n">cmap</span><span class="o">=</span><span class="s2">&quot;gray&quot;</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">plt</span><span class="o">.</span><span class="n">imshow</span><span class="p">(</span><span class="n">activation</span><span class="p">[</span><span class="mi">0</span><span class="p">,:,:,</span> <span class="n">featuremap</span><span class="p">],</span> <span class="n">interpolation</span><span class="o">=</span><span class="s2">&quot;nearest&quot;</span><span class="p">,</span> <span class="n">cmap</span><span class="o">=</span><span class="s2">&quot;gray&quot;</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

</div>
    </div>
  </div>
</body>

 


</html>
```
