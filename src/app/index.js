var React = require('react');
var ReactDOM = require('react-dom');

var SearchBar = require('./searchBar');
var SubSearchBar = require('./subSearchBar');

class SearchComponent extends React.Component{
    constructor(){
        super();
        this.onSubmit = this.onSubmit.bind(this);
    }

    render(){
        return(
            <div id="search-bar">
                <SearchBar></SearchBar>
                <SubSearchBar></SubSearchBar>
            </div>
        );
    }

    onSubmit(e){
        e.preventDefault();
        
    }
}

ReactDOM.render(<SearchComponent />, document.getElementById('search-wrapper'));