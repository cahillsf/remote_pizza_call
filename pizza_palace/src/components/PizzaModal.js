import React from "react";
export default class PizzaModal extends React.Component {
  render() {
    console.log(this.props)
    if(!this.props.show){
      return null;
    }
    return <div>Hello Modal</div>;
  }
}