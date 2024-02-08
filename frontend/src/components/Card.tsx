import '../base.css'

export interface CardProps {
  id: number
  title: string
  body: string
}

function Card({id, title, body}: CardProps) {
  
  console.log('Getting card with id: ' + id + ' , title: ' + title + ' , body: ' + body)

  return (
    <div className='bg-gray-500 rounded-lg w-auto m-4 p-2'>
      <h3 className='text-gray-100 font-bold mb-2'>{title}</h3>
      <p className='text-gray-100'>{body}</p>
    </div>
  )
}

export default Card