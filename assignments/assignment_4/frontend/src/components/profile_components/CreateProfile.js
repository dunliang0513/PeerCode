import React, { useRef, useState } from 'react'
import { Col, Button, Row, Container, Card, Form, Alert } from 'react-bootstrap';
import { useAuth } from '../../contexts/AuthContext';
import { Link } from 'react-router-dom';

import Axios from 'axios';

export default function CreateProfile() {
  const displayNameRef = useRef();
  const usernameRef = useRef();
  const proficiencyLevelRef = useRef();
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false)
  const [message, setMessage] = useState("");
  const [hasCreated, setHasCreated] = useState(false)
  const { currentUser } = useAuth();


  function createUserProfile(event) {
    event.preventDefault();
    const user = {
      email: currentUser.email,
      displayName: displayNameRef.current.value,
      username: usernameRef.current.value,
      proficiency: proficiencyLevelRef.current.value
    }

    Axios.post("http://localhost:3001/insert", { user })
      .then(res => {
        setLoading(true);
      })
      .catch(err => {
        setError("Error occurred, try again later!");
      })
    setLoading(false);
    if (error === "") {
      setMessage("Profile created successfully!");
      setHasCreated(true);
    }
  }

  return (
    <>
      <Container>
        <Row className="vh-100 d-flex justify-content-center align-items-center">
          <Col md={8} lg={6} xs={12}>
            {error && <Alert variant="danger">{error}</Alert>}
            {message && <Alert variant="success">{message}</Alert>}
            <div className="border border-3 border-primary"></div>
            <Card className="shadow">
              <Card.Body>
                <div className="mb-3 mt-4">
                  <h2 className="fw-bold mb-2 text-uppercase">Create Profile</h2>
                  <p className=" mb-5">Customise your profile here!</p>

                  <Form className="mb-3" onSubmit={createUserProfile}>

                    <Form.Group className="mb-3" controlId="formDisplayName">
                      <Form.Label className="text-center">Display Name</Form.Label>
                      <Form.Control type="text" ref={displayNameRef} placeholder="Enter your Display Name" />
                    </Form.Group>

                    <Form.Group className="mb-3" controlId="formUserName">
                      <Form.Label className="text-center">Username</Form.Label>
                      <Form.Control type="text" ref={usernameRef} placeholder="Enter your Username" />
                    </Form.Group>

                    <Form.Group className="mb-3" controlId="formProficiencyLevel">
                      <Form.Label className="text-center">Proficiency Level</Form.Label>
                      <Form.Select ref={proficiencyLevelRef}>
                        <option>Expert</option>
                        <option>Intermediate</option>
                        <option>Beginner</option>
                      </Form.Select>
                    </Form.Group>

                    <div className="d-grid">
                      {!hasCreated && <Button disabled={loading} variant="primary" type="submit">Create Profile</Button>}
                    </div>
                  </Form>
                  <Link to="/profile" className="btn btn-primary w-100 mt-3">Back</Link>
                </div>
              </Card.Body>
            </Card>
          </Col>
        </Row>
      </Container>
    </>
  )
}
