import React from 'react'

const Footer: React.FC = () => {
  return (
    <footer style={{
      textAlign: 'center',
      padding: '15px 20px',
      backgroundColor: '#f0f0f0',
      color: '#333',
      marginTop: 'auto'
    }}>
      <p style={{ fontSize: '0.9rem' }}>
        &copy; {new Date().getFullYear()} MyDiabetesProject. All rights reserved.
      </p>
    </footer>
  )
}

export default Footer
