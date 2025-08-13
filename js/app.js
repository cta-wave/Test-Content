function eq(a, b) {
  return a == b;
}

function lt(a, b) {
  return a < b;
}

function lte(a, b) {
  return a <= b;
}

function gt(a, b) {
  return a > b;
}

function gte(a, b) {
  return a >= b;
}

function diff(a, b) {
  return a != b;
}

const comps = {
  ">=": gte,
  "==": eq,
  "<": lt,
  ">": gt,
  "<=": lte,
  "!=": diff
}

function tokenize(s) {
  let searches = s.split(":");
  if (searches.length == 0)
    return undefined;

  let terms = []
  for (let i = 0; i < searches.length; i++) {
    let match = searches[i].match(/^([a-zA-Z0-9_+\-\/* ]+)\s*(>=|<=|>|<|==|!=)\s*([a-zA-Z0-9_+\-\/* ]+)$/)
    if (match.length != 4) {
      continue;
      // malformed
    }
    terms.push({ func: comps[match[2]], term1: match[1], term2: match[3] });
  }
  return terms;
}

$.getJSON("https://raw.githubusercontent.com/cta-wave/Test-Content/master/database.json", function (data) {
  var player = dashjs.MediaPlayer().create();
  let app = new Vue({
    el: '#app',
    data: {
      database: data,
      search: '',
      results_cfhd:          data["CFHD"],
      results_chdf:          data["CHDF"],
      results_chh1:          data["CHH1"],
      results_cenc:          data["CENC"],
      results_cfhd_splicing: data["CFHD-SPLICING"],
      results_ceac:          data["CEAC"],
      results_ca4s:          data["CA4S"],
      results_caac:          data["CAAC"],
      results_caaa:          data["CAAA"],
      results_camc:          data["CAMC"],
      results_dts1:          data["DTS1"],
      results_chunked:       data["chunked"],
      results_chh1_splicing: data["CHH1_SPLICING"],
      results_cud1:          data["CUD1"],
      results_cud1_splicing: data["CUD1_SPLICING"],
      results_clg1:          data["CLG1"],
      results_clg1_splicing: data["CLG1_SPLICING"],
      results_chd1:          data["CHD1"],
      results_chd1_splicing: data["CHD1_SPLICING"],
    },
    methods: {
      play: function(mpd) {
        player.initialize(document.querySelector("#videoPlayer"), mpd, true);
      },
      searchInDB: function (e) {
        let tokens = tokenize(this.search);
        this.results = Object.values(this.database).filter(element => {
          var cond = true;
          var hasBeenIn = false;
          tokens.forEach((token) => {
            //todo implement OR and more complex searches
            cond = cond && token.func(element[token.term1], token.term2);
            hasBeenIn = true;
          })
          return hasBeenIn && cond;

        });
        console.log(results.length)
        e.preventDefault();
      }
    }
  })
});
