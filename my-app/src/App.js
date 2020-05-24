import React, { Component } from 'react';
import Songlist from './songlist.js';
import InputForm from './input'
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';

class App extends Component {



  render() {
    return (
      <div className="App">
        <InputForm></InputForm>
        <Songlist></Songlist>

      </div>
    );

  }

}



export default App;
