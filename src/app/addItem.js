var React = require('react');
require('./addItem.css')

class AddItem extends React.Component{
    constructor(){
        super();
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    render(){
        return(
            <form id="add-todo" onSubmit={this.handleSubmit}>
                <input type="text" required ref="newItem" />
                <input type="submit" value="Hit me" onClick={this.handleSubmit}/>
            </form>
        );
    }

    handleSubmit(e){
        e.preventDefault(); // stop normal behaviour of submit button, ie. don't reload page
        this.props.onAdd(this.refs.newItem.value);
    };
}

module.exports = AddItem