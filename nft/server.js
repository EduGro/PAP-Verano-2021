const koa = require('koa');
const cors = require('@koa\cors');
const serve = require('koa-static');
const { ProvidePlugin } = require('webpack');
const router = require('.\router.js');

const app = new koa();

app
  .use(cors())
  .use(serve('.\images'))
  .use(router.routes());

pp.listen(process.env.PORT || 3000);