var React = require('react');
require('./todoItem.css');

class TodoItem extends React.Component{
    constructor(){
        super();
        this.handleDelete = this.handleDelete.bind(this);
    }
    render(){
        return(
            <li>
                <div className="todo-item">
                    <span className="item-name">{this.props.item}</span>
                    <span className="item-delete" onClick={this.handleDelete}> x</span>
                </div>
            </li>
        );
    } // render

    handleDelete(){
        //console.log(this.props.item);
        this.props.onDelete(this.props.item);
    }
};

module.exports = TodoItem;