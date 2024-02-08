import '../base.css'
import Column from './Column'


const columns = [
	{
		'id': 1, 
		'boardId': 1,
		'name': 'To Do'
	},
	{
		'id': 2, 
		'boardId': 1,
		'name': 'In Progress'
	},
	{
		'id': 3, 
		'boardId': 1,
		'name': 'Done'
	}
]

function Board() {
	// get columns of this board
	const getColumns = () => {
		return columns
	}

	return (
		<div className='flex'>
			{getColumns().map((column) => {
				return (
					<Column key={column.id} id={column.id} boardId={column.boardId} name={column.name}></Column>
				)
			})}
		</div>
	)
}

export default Board