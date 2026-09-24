import { defineConfig } from "@playwright/test";

export default defineConfig({
    testMatch: "scraper.ts",
    use:{
        screenshot: "on",
        // video:"retain-on-failure"
    },
    reporter: [["dot"],["json",{
        outputFile: "jsonReports/jsonReport.json"
    }
    ],["html",{
        open:"always"
    }]]
});