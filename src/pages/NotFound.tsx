import React from 'react'

const NotFound: React.FC = () => {
  return (
    <div style={{
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      justifyContent: 'center',
      height: '80vh',
      fontFamily: 'Arial, sans-serif'
    }}>
      <h1 style={{ fontSize: '2rem', marginBottom: '1rem' }}>404 - Not Found</h1>
      <p style={{ fontSize: '1rem' }}>
        The page you are looking for doesn't exist or might have been moved.
      </p>
    </div>
  )
}

export default NotFound
