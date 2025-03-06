import React from 'react'
import { Link } from 'react-router-dom'

const Header: React.FC = () => {
  return (
    <header style={{
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'space-between',
      backgroundColor: '#007bff',
      color: '#fff',
      padding: '10px 20px'
    }}>
      <div style={{ fontSize: '1.2rem', fontWeight: 'bold' }}>
        MyDiabetesProject
      </div>
      <nav>
        <Link
          to="/"
          style={{
            marginRight: '15px',
            color: '#fff',
            textDecoration: 'none'
          }}
        >
          Home
        </Link>
        <Link
          to="/about"
          style={{
            color: '#fff',
            textDecoration: 'none'
          }}
        >
          About
        </Link>
      </nav>
    </header>
  )
}

export default Header
