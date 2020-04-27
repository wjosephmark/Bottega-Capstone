import React, { Component } from 'react';
import { BrowserRouter as Router, Switch, Route } from "react-router-dom"

import Home from "./pages/home"
import Tools from "./pages/tools"
import Sites from "./pages/sites"
import Checkout from "./pages/checkout"
import NoMatch from "./pages/no-match"

export default class App extends Component {
  render() {
    return (
      <div className='app'>
        <Switch>

          <Route exact path="/" component={Home} />
          <Route path="/tools" component={Tools} />
          <Route path="/sites" component={Sites} />
          <Route path="/checkout" component={Checkout} />
          <Route component={NoMatch} />

        </Switch>
      </div>
    );
  }
}
