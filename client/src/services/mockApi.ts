import webpackMockServer from "webpack-mock-server";
import nodePath from "path";
import cors from 'cors';

// app is expressjs application
export default webpackMockServer.add((app, helper) => {
  app.use(cors());

  app.get("/api/metrics/", (_req, res) => {
    res.sendFile(nodePath.join(__dirname, "../mocks/data/metrics.json"));
  });
});