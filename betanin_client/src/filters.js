import Vue from "vue";

const filters = {
  formatTimestamp(timestamp) {
    const datetime = new Date(timestamp);
    return datetime.toLocaleTimeString("en-IE");
  },
  lower(string) {
    return string.toLowerCase();
  },
  toYesNo(value) {
    return value ? "yes" : "no";
  },
  round(value) {
    return Math.round(value);
  },
  truncate(text, stop, clamp) {
    if (!text) {
      return "";
    }
    return text.slice(0, stop) + (stop < text.length ? clamp || "..." : "");
  },
};

Object.keys(filters).forEach((filterName) => {
  Vue.filter(filterName, filters[filterName]);
});
