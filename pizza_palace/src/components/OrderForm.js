import React from 'react';
import Pizza from '../classes/Pizza2'
import PizzaModal from './PizzaModal';
import axios from 'axios';

export default class OrderForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      showModal: false,
      name: '',
      email: '',
      pizza: new Pizza("large","none"),
      pizzas: []
    };
    console.log(this.state.pizza)
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.addPizza = this.addPizza.bind(this);
  }

  addPizza(){
    this.setState({
      showModal: true,
    })
  }

  handleChange(event) {
    const target = event.target;
    const name = target.name;
    const value = target.value;
    console.log(value);
    if (name === "pizzasize") {
      // let newPizza = new Pizza({size: value})
      let newPizza = new Pizza(value, "PEPPERS");
      console.log(newPizza); 
      this.setState({
        pizza: newPizza,
      });
    }
    else if (name === "addPizza"){
      this.setState({
        showModal: true,
      })
    }
    else{
      this.setState({
        [name]: value
      });
    }
    console.log(this.state)
  }
  

  handleSubmit(event) {
    alert('A name was submitted: ' + this.state.name);
    this.state.pizzas.push(this.state.pizza);
    this.sendToServer(event);
    console.log(this.state);
    event.preventDefault();
    event.target.reset();
  }

  async sendToServer(event) {
    console.log("sending to server");
    console.log(event);
    console.log(this.state);
    try {
      const response = await axios
          .post(
              "http://localhost:8000/api/test",
              this.state
          )
          .catch(function(error) {
            console.log(error);
          });
      console.log(response);
      return;
    } catch (error) {
      console.log(error);
    }
  }

  render() {
    return (
      <div>
        <form onSubmit={this.handleSubmit}>
          <label>
            Name:
            <input type="text" name="name" value={this.state.name} onChange={this.handleChange} />
          </label>
          <label>
            Email:
            <input type="text" name="email" value={this.state.email} onChange={this.handleChange} />
          </label>
          <label>
            Pick your pizza size:
            <select name="pizzasize" value={this.state.pizza.size} onChange={this.handleChange}>
              <option value="SMALL">Small</option>
              <option value="MEDIUM">Medium</option>
              <option value="LARGE">Large</option>
            </select>
          </label>
          <input type="submit" value="Submit" />
        </form>
        <button onClick={this.sendToServer}>Send to Server</button>
        <button name="addPizza" onClick={this.addPizza}>Add a Pizza</button>
        <PizzaModal show={this.state.showModal} />
      </div>
    );
  }
}