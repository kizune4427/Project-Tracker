import '../base.css'
import Card, {CardProps} from './Card'

const cards = [
  {
    'id': 1, 
    'title': 'First Card',
    'body': 'This is the body of the first card',
    'created_at': '2021-07-01'
  },
  {
    'id': 2, 
    'title': 'Second Card',
    'body': 'This is the body of the second card',
    'created_at': '2021-07-02'
  }
]

export interface ColumnProps {
  id: number
  boardId: number
  name: string
}

function Column({id, boardId, name}: ColumnProps) {
    
  const getCards = () => {
    console.log('Getting cards for columnId: ' + id + ' , boardId: ' + boardId + ' , name: ' + name)
    return cards
  }

  return (
      <div className='flex-col w-48 bg-gray-800 m-4 p-2 rounded-lg'>
        <h3 className='text-gray-100 font-extrabold mx-4 mb-2'>{name}</h3>
        {getCards().map((card: CardProps) => {
          return (
            <Card key={card.id} id={card.id} title={card.title} body={card.body}></Card>
          )
        })}
      </div>
    )
}

export default Column