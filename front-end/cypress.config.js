const { defineConfig } = require("cypress");

module.exports = defineConfig({
  projectId: "862v9w",
  e2e: {
    baseUrl: 'http://localhost:3000'
  },
});
