import React from 'react'
import { Link } from 'react-router-dom'

const Sidebar: React.FC = () => {
  return (
    <aside style={{
      width: '200px',
      backgroundColor: '#f7f7f7',
      borderRight: '1px solid #ccc',
      padding: '20px',
      height: '100vh',
      boxSizing: 'border-box'
    }}>
      <nav style={{ display: 'flex', flexDirection: 'column' }}>
        <Link
          to="/"
          style={{
            marginBottom: '10px',
            textDecoration: 'none',
            color: '#333'
          }}
        >
          Home
        </Link>
        <Link
          to="/about"
          style={{
            marginBottom: '10px',
            textDecoration: 'none',
            color: '#333'
          }}
        >
          About
        </Link>
      </nav>
    </aside>
  )
}

export default Sidebar
