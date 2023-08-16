import '../global/globals.css'
import styles from '../styles/style.module.css'
import { Inter } from 'next/font/google'

const inter = Inter({ subsets: ['latin'] })

export const metadata = {
  title: 'ProjectSpark Dashboard Application',
  description: 'Project Spark is an innovative platform that allows developers to capture and share ideas for software projects, providing a space for collaboration and project management.',
}

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className={`${inter.className}`}>{children}</body>
    </html>
  )
}
